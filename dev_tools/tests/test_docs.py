import pytest

from ..docs import AnchorRegistry
from ..docs import NXClassDocGenerator
from ..docs import XSDDocGenerator
from ..docs import nxdl_indices
from ..globals.directories import get_xsd_file
from ..nxdl import iter_definitions

SKIP_FILES_FROM_TESTS = [
    "NXhdf5_validator_2.nxdl.xml",
    "NXhdf5_validator_1.nxdl.xml",
]


@pytest.fixture(scope="module")
def doc_generator():
    return NXClassDocGenerator()


@pytest.fixture(scope="module")
def anchor_registry():
    return AnchorRegistry()


@pytest.fixture(scope="module")
def anchor_registry_write(tmpdir_factory):
    tmpdir = tmpdir_factory.mktemp("registry")
    reg = AnchorRegistry(output_path=tmpdir)
    yield reg
    reg.write()


@pytest.mark.parametrize("nxdl_file", list(iter_definitions()))
def test_nxdl_generate_doc(nxdl_file, doc_generator):
    if nxdl_file.name in SKIP_FILES_FROM_TESTS:
        pytest.skip(f"Skip {nxdl_file.name}")
    assert doc_generator(nxdl_file)


@pytest.mark.parametrize("nxdl_file", list(iter_definitions()))
def test_nxdl_anchor_list(nxdl_file, doc_generator, anchor_registry):
    if nxdl_file.name in SKIP_FILES_FROM_TESTS:
        pytest.skip(f"Skip {nxdl_file.name}")
    assert doc_generator(nxdl_file, anchor_registry=anchor_registry)


@pytest.mark.parametrize("nxdl_file", list(iter_definitions()))
def test_nxdl_anchor_write_list(nxdl_file, doc_generator, anchor_registry_write):
    if nxdl_file.name in SKIP_FILES_FROM_TESTS:
        pytest.skip(f"Skip {nxdl_file.name}")
    assert doc_generator(nxdl_file, anchor_registry=anchor_registry_write)


def test_nxdl_indices():
    sections = nxdl_indices()
    expected = {"base_classes", "applications", "contributed_definitions"}
    assert set(sections) == expected


def test_xsd_generate_doc():
    generator = XSDDocGenerator()
    assert generator(get_xsd_file())
