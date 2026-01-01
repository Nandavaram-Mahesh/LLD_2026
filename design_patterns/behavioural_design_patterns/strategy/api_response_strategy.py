import json, xml.etree.ElementTree as ET, yaml
from abc import ABC , abstractmethod
# Abstract Strategy
class ResponseFormatter(ABC):
    @abstractmethod
    def format(self, data): pass

# Concrete Strategies
class JSONFormatter(ResponseFormatter):
    def format(self, data):
        return json.dumps(data)

# Concrete Strategies
class XMLFormatter(ResponseFormatter):
    def format(self, data):
        root = ET.Element("response")
        for k, v in data.items():
            ET.SubElement(root, k).text = str(v)
        return ET.tostring(root, encoding="unicode")

# Concrete Strategies
class YAMLFormatter(ResponseFormatter):
    def format(self, data):
        return yaml.dump(data)

# Context
class APIResponse:
    def __init__(self, formatter: ResponseFormatter):
        self.formatter = formatter

    def send(self, data):
        return self.formatter.format(data)


# ✅ Usage
response = APIResponse(YAMLFormatter())
print(response.send({"status": "ok", "code": 200}))
