from rest_framework import serializers as rf


def lxml_to_dict(node):
    """
    Convert an lxml.etree node tree into a dict.
    """
    storage = {}

    for e in node.iterchildren():
        key = e.tag.split('}')[1] if '}' in e.tag else e.tag
        storage[key] = e.text if e.text else lxml_to_dict(e)

    return storage


class DequeToDictMixin:
    def to_internal_value(self, data):
        return {item.tag: lxml_to_dict(item) for item in data}


class MRNSerializer(DequeToDictMixin, rf.Serializer):
    mrn = rf.SerializerMethodField()

    def get_mrn(self, obj):
        return obj['HEAHEA']['DocNumHEA5']
