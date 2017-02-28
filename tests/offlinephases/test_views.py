import io

import pytest
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse

from euth.offlinephases import models as offlinephase_models


@pytest.fixture
def pdf_file():
    bytes = io.BytesIO(
        b'%PDF-1.1\n'
        b'%\xc2\xa5\xc2\xb1\xc3\xab\n'
        b'\n'
        b'1 0 obj\n'
        b'  << /Type /Catalog\n'
        b'     /Pages 2 0 R\n'
        b'  >>\n'
        b'endobj\n'
        b'\n'
        b'2 0 obj\n'
        b'  << /Type /Pages\n'
        b'     /Kids [3 0 R]\n'
        b'     /Count 1\n'
        b'     /MediaBox [0 0 300 144]\n'
        b'  >>\n'
        b'endobj\n'
        b'\n'
        b'3 0 obj\n'
        b'  <<  /Type /Page\n'
        b'      /Parent 2 0 R\n'
        b'      /Resources\n'
        b'       << /Font\n'
        b'           << /F1\n'
        b'               << /Type /Font\n'
        b'                  /Subtype /Type1\n'
        b'                  /BaseFont /Times-Roman\n'
        b'               >>\n'
        b'           >>\n'
        b'       >>\n'
        b'      /Contents 4 0 R\n'
        b'  >>\n'
        b'endobj\n'
        b'\n'
        b'4 0 obj\n'
        b'  << /Length 55 >>\n'
        b'stream\n'
        b'  BT\n'
        b'    /F1 18 Tf\n'
        b'    0 0 Td\n'
        b'    (Hello World) Tj\n'
        b'  ET\n'
        b'endstream\n'
        b'endobj\n'
        b'\n'
        b'xref\n'
        b'0 5\n'
        b'0000000000 65535 f \n'
        b'0000000018 00000 n \n'
        b'0000000077 00000 n \n'
        b'0000000178 00000 n \n'
        b'0000000457 00000 n \n'
        b'trailer\n'
        b'  <<  /Root 1 0 R\n'
        b'      /Size 5\n'
        b'  >>\n'
        b'startxref\n'
        b'565\n'
        b'%%EOF\n'
    )
    return InMemoryUploadedFile(
        bytes, None, 'minimal.pdf', 'application/pdf', None, None
    )


@pytest.mark.django_db
def test_initiator_can_edit_offlinephase(client, offlinephase, pdf_file):
    op_documentation = offlinephase

    user = offlinephase.phase.module.project.moderators.first()
    client.login(username=user.email, password='password')

    url = reverse('offlinephase-edit', kwargs={'pk': op_documentation.pk})
    response = client.get(url)
    assert response.status_code == 200

    response = client.post(url, {
        'fileuploads-TOTAL_FORMS': '1',
        'fileuploads-INITIAL_FORMS': '0',
        'fileuploads-MIN_NUM_FORMS': '0',
        'fileuploads-MAX_NUM_FORMS': '5',
        'fileuploads-0-title': 'title',
        'fileuploads-0-document': pdf_file,
        'offlinephase-text': 'Lorem ipsum'
    })
    assert response.status_code == 302

    fileupload = offlinephase_models.FileUpload.objects.get(
        offlinephase=op_documentation
    )
    assert fileupload.title == 'title'
