# Contacts-Parser

Detta program konverterar filer med följande format:
```txt
P|Carl Gustaf|Bernadotte  
T|0768-101801|08-101801  
A|Drottningholms slott|Stockholm|10001  
F|Victoria|1977  
A|Haga Slott|Stockholm|10002  
F|Carl Philip|1979  
T|0768-101802|08-101802  
P|Barack|Obama  
A|1600 Pennsylvania Avenue|Washington, D.C  
```

Till XML:

```xml
<?xml version="1.0" encoding="utf-8"?>
<people>
  <person>
    <firstname>Carl Gustaf</firstname>
    <lastname>Bernadotte</lastname>
    <phone>
      <mobile>0768-101801</mobile>
      <landline>08-101801</landline>
    </phone>
    <address>
      <street>Drottningholms slott</street>
      <city>Stockholm</city>
      <zip>10001</zip>
    </address>
    <family>
      <name>Victoria</name>
      <birthyear>1977</birthyear>
    </family>
    <address>
      <street>Haga Slott</street>
      <city>Stockholm</city>
      <zip>10002</zip>
    </address>
    <family>
      <name>Carl Philip</name>
      <birthyear>1979</birthyear>
    </family>
    <phone>
      <mobile>0768-101802</mobile>
      <landline>08-101802</landline>
    </phone>
  </person>
  <person>
    <firstname>Barack</firstname>
    <lastname>Obama</lastname>
    <address>
      <street>1600 Pennsylvania Avenue</street>
      <city>Washington, D.C</city>
    </address>
  </person>
</people>
```
