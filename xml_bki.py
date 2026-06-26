import xml.etree.ElementTree as ET

#загрузка и чтение XML-файлов (заявки)
tree_application = ET.parse('applications.xml')
root_application = tree_application.getroot()

#загрузка и чтение XML-файлов (договоры)
tree_contract = ET.parse('contracts.xml')
root_contract = tree_contract.getroot()

#Работа с Namespaces
xml_ns = '{http://cbr.ru}'  #(Сюда вставляется актуальный xmlns из рабочих файлов)

uuid_application = set()
uuid_contract = set()
invalid_contracts = set()

#Сбор UUID из файла заявок
for application in root_application.iter(f'{xml_ns}InfoPart'):
    uuid_tag_a = application.find(f'{xml_ns}Uuid')
    uuid_application.add(uuid_tag_a.text.strip().lower())
#Сбор UUID из файла договоров
for contract in root_contract.iter(f'{xml_ns}Trade'):
    uuid_tag_c = contract.find(f'{xml_ns}Uuid')
    uuid_contract.add(uuid_tag_c.text.strip().lower())

#Поиск договоров, для которых не были найдены заявки
invalid_contracts = uuid_contract - uuid_application

#Вывод договоров без заявок
print(f'UUID договоров, к которым отсутствует заявка: {invalid_contracts}')
