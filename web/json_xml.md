# JSON 
Java Script Object Notation (Javascript 객체 문법)으로 <b><i>구조화된 데이터 교환 형식</b></i>

JSON in JS
```javascript
{
    "name" : "hee",
    "age" : 30,
    "school" : "hkust"
}

{
    "OST":
    [
        {
            "song":"song name1",
            "length":124
        },
        {
            "song":"song name2",
            "length": "LONG!" //return type doesn't matter
        }
    ]
}

jsonObject.OST[0].song // "song name1"
jsonObject.OST[1].length // "LONG!"


```

- Used in various languages (object, hash table, dictionary)
- Independent of programming language / framework - python version will not affect json

## Usage of JSON
1. Return type for APIs
```JSON
//UPBIT
{
    "currency":"KRW",
    "balance":"1000000.0",
    "locked":"0.0",
    "avg_buy_price":"0",
    "avg_buy_price_modified":false,
    "unit_currency": "KRW",
  }
```
2. System config file (npm package.json)

# XML 
Extensible Markup Language은 <b><i>마크업 형태를 쓰는 데이터 교환 형식</b></i> - 태그를 사용함

```xml
<?xml version = "1.0" encoding="UTF-8"?>
<OST>
    <song>song name1</song><length>124</length>
    <song>song name2</song><length>130</length>
</OST>
```

- Similar to HTML but HTML requires predefined tags. XML allows custom tags.

## Usage of XML
- Used for sitemap.xml. 
- sitemap.xml is data that lists all the pages inside a service. 
- When links aren't connected, crawler might skip pages. sitemap.xml prevents this and allows the crawler to go through all pages

# JSON vs XML
- XML is heavier due to opening tag, closing tag.
- XML requires external package for serialization while JSON has built in methods for serialization.