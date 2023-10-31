from pathlib import Path

import lxml.etree as ET
from click.testing import CliRunner

from ..nyaml2nxdl import nyaml2nxdl as conv
from ..nyaml2nxdl.nyaml2nxdl_helper import remove_namespace_from_tag
from ..utils.nxdl_utils import find_definition_file


def test_conversion():
    root = find_definition_file("NXentry")
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(root)])
    assert result.exit_code == 0
    # Replace suffixes
    yaml = root.with_suffix("").with_suffix(".yaml")  # replace .nxdl.xml
    yaml = yaml.with_stem(yaml.stem + "_parsed")  # extend file name with _parsed
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(yaml)])
    assert result.exit_code == 0
    new_root = yaml.with_suffix(".nxdl.xml")  # replace yaml
    with open(root, encoding="utf-8", mode="r") as tmp_f:
        root_content = tmp_f.readlines()
    with open(new_root, encoding="utf-8", mode="r") as tmp_f:
        new_root_content = tmp_f.readlines()
    assert root_content == new_root_content
    yaml.unlink()
    new_root.unlink()


def test_doc():
    """To test the doc style."""
    pwd = Path(__file__).parent

    doc_file = pwd / "data/doc_test.yaml"
    ref_doc_file = pwd / "data/ref_doc_test.nxdl.xml"
    out_doc_file = pwd / "data/doc_test.nxdl.xml"
    result = CliRunner().invoke(conv.launch_tool, ["--input-file", str(doc_file)])

    assert result.exit_code == 0, f"Error: Having issue running input file {doc_file}."

    ref_nxdl = ET.parse(str(ref_doc_file)).getroot()
    out_nxdl = ET.parse(str(out_doc_file)).getroot()

    def compare_doc(parent1, parent2):
        if len(parent1) > 0 and len(parent2) > 0:
            for par1, par2 in zip(parent1, parent2):
                compare_doc(par1, par2)

        elif (
            remove_namespace_from_tag(parent1.tag) == "doc"
            and remove_namespace_from_tag(parent2.tag) == "doc"
        ):
            assert (
                parent1.text == parent2.text
            ), f"DOCS ARE NOT SAME: node {parent1}, node {parent2}"

    compare_doc(ref_nxdl, out_nxdl)
    out_doc_file.unlink()
