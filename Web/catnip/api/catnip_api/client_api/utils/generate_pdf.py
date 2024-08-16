# ATTRIBUTION: https://github.com/c53elyas/CVE-2023-33733
from reportlab.platypus import SimpleDocTemplate, Paragraph
from io import BytesIO

def generate_pdf(body_content: str, shelter_name: str, cat_count: int):
    stream_file = BytesIO()
    content = []

    def add_paragraph(text, content):
        """ Add paragraph to document content"""
        content.append(Paragraph(text))

    def get_document_template(stream_file: BytesIO):
        """ Get SimpleDocTemplate """
        return SimpleDocTemplate(stream_file)

    def build_document(document, content, **props):
        """ Build pdf document based on elements added in `content`"""
        document.build(content, **props)


    doc = get_document_template(stream_file)
    add_paragraph("<h1>Cat Cafe Adoption Request</h1><br/><br/>", content)
    add_paragraph(f"Cat Cafe is requesting to adopt {cat_count} new cat{cat_count > 1 and 's' or ''} from {shelter_name}.<br/>See reason as attached below: <br/><br/>", content)
    add_paragraph(body_content, content)
    build_document(doc, content)

    return stream_file.getvalue()
