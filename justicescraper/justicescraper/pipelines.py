# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JusticescraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)

        ## Strip all whitespaces from strings
        field_names = adapter.field_names()
        text_keys = ['node_component', 'office', 'subtitle']
        for text_key in text_keys:
            value = adapter.get(text_key)
            if value is not None:
                adapter[text_key] = value.strip()


        for field_name in field_names:
            if field_name == 'date':
                value = adapter.get(field_name)
                adapter[field_name] = value.replace("Updated ", "")
            

        return item
