import xml.etree.cElementTree as et
patent_root_tag = et.parse('single_patent_file.xml').getroot()

bibliography_grant_tag = 'us-bibliographic-data-grant'
bibliography_application_tag = 'us-bibliographic-data-application'
for child_tag in patent_root_tag:
    if child_tag.tag == bibliography_grant_tag or child_tag.tag == bibliography_application_tag:

        list_of_bibliography_tags = list(child_tag.iter())
        for sub_child in list_of_bibliography_tags:

            print(sub_child.tag,":",sub_child.text)