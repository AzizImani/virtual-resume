from pypdf import PdfReader


class KnowledgeSource:
    __resume = "me/linkedin.pdf"
    __summary = "me/summary.txt"
    __name = "Abdelaziz Imani"

    @classmethod
    def load_resume(cls) -> str:
        reader = PdfReader(cls.__resume)
        content = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                content += text
        return content

    @classmethod
    def load_summary(cls) -> str:
        with open(cls.__summary, "r", encoding="utf-8") as f:
            return f.read()

    @classmethod
    def load_name(cls) -> str:
        return cls.__name
