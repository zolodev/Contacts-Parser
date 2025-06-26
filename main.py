import xml.dom.minidom  # Prettify (läsbar xml output)
import xml.etree.ElementTree as ET

data = """
P|Carl Gustaf|Bernadotte
T|0768-101801|08-101801
A|Drottningholms slott|Stockholm|10001
F|Victoria|1977
A|Haga Slott|Stockholm|10002
F|Carl Philip|1979
T|0768-101802|08-101802
P|Barack|Obama
A|1600 Pennsylvania Avenue|Washington, D.C
"""

# För att hantera tomma värden, eller värden som saknas.
def safe_add(parent, tag, value):
    if value.strip():  # Lägg bara till om det inte är tomt eller bara mellanslag
        ET.SubElement(parent, tag).text = value

# Alternative 2 läsa in från fil, måste byta ut data.splitlines() till lines i for-loopen
# with open("contacts.txt", "r", encoding="utf-8") as f:
#     lines = f.readlines()

root = ET.Element("people")
current_person = None

# Alternativ 2
# for line in lines():
for line in data.splitlines():
    parts = line.strip().split('|')
    code = parts[0]

    # Hantera enskild person, för- och efternamn
    if code == 'P' and len(parts) >= 3:
        current_person = ET.SubElement(root, "person")
        safe_add(current_person, "firstname", parts[1])
        safe_add(current_person, "lastname", parts[2])

    # Hantera telfonnummer, mobil och fastland
    elif code == 'T' and len(parts) >= 2:
        phone = ET.SubElement(current_person, "phone")
        safe_add(phone, "mobile", parts[1])
        if len(parts) >= 3:
            safe_add(phone, "landline", parts[2])

    # Hantera adress
    elif code == 'A' and len(parts) >= 3:
        address = ET.SubElement(current_person, "address")
        safe_add(address, "street", parts[1])
        safe_add(address, "city", parts[2])
        if len(parts) > 3:
            safe_add(address, "zip", parts[3])

    # Hantera familjemedlemma (barn)
    elif code == 'F' and len(parts) >= 3:
        family = ET.SubElement(current_person, "family")
        safe_add(family, "name", parts[1])
        safe_add(family, "birthyear", parts[2])


# skriv ut xml, med stöd av unicode, alternativt med utf-8, dock medför detta en b' eftersom outputen är binär.
# Däremot är det viktigt att använda utf-8 om man skriver till fil och för att behålla specialtecken som å,ä och ö
xml_str = ET.tostring(root, encoding='unicode', method='xml')

# Print RAW (one-liner)
print(xml_str)

# Prettify XML
reparsed = xml.dom.minidom.parseString(xml_str)
pretty_xml = reparsed.toprettyxml()

# Skriv ut läsbar XML
print(pretty_xml)

# Spara till fil med XML-deklaration
with open("output.xml", "w", encoding="utf-8") as f:
    f.write(pretty_xml)
