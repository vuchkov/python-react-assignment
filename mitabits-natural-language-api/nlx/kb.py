import hashlib

import yaml


class Object(object):
    def __init__(self, uuid, name, properties):
        self._uuid = uuid
        self._name = name
        self._properties = properties

    def as_html(self):
        return f"<h5>{self.name}</h5>" + "".join(
            [f"<div><strong>{name}</strong>: {value}" for name, value in self.iter_properties()])

    @property
    def uuid(self):
        return self._uuid

    @property
    def name(self):
        return self._name

    @property
    def synonyms(self):
        return list(set([s.strip() for s in self._properties.get('synonyms', "").split(",") if s.strip()]))

    def iter_properties(self):
        return self._properties.items()

    def as_dict(self):
        return dict(name=self.name, **self._properties)


class SearchResult(object):
    def __init__(self, obj, score=1.0):
        self.obj = obj
        self.score = score
        if score > 1:
            raise ValueError("Invalid score!")

    def as_dict(self):
        return {
            "score": self.score,
            "object": {
                "name": self.obj.name,
                "properties": dict(self.obj.iter_properties()),
                "html": self.obj.as_html()
            }
        }


class ObjectStorage(object):
    def __init__(self, filepath, object_class):
        super().__init__()
        self._filepath = filepath
        self._object_class = object_class
        self._name_hashmap = {}
        self._objects = {}
        self._read_yaml()

    def _read_yaml(self):
        self._objects = {}
        with open(self._filepath, 'r') as fp:
            self._data = yaml.load(fp, Loader=yaml.FullLoader)
            for name, props in self._data.items():
                self.add(name, props)

    @staticmethod
    def generate_id(name):
        return hashlib.sha256(name.encode()).hexdigest()

    @property
    def objects(self):
        return list(self._objects.values())

    def iter_objects(self):
        return self._objects.items()

    @property
    def object_class(self):
        return self._object_class

    def add(self, name, props):
        obj = Object(self.generate_id(name), name, props)
        self._objects[obj.uuid] = obj
        self._name_hashmap[name] = obj.uuid
        return obj.uuid

    def get(self, object_id):
        return self._objects[object_id]

    def get_by_name(self, object_name):
        if object_name not in self._name_hashmap:
            raise ValueError(f"Object with NAME={object_name} does not exist.")
        return self._objects[self._name_hashmap[object_name]]

    def search(self, search_query):
        try:
            return [SearchResult(self.get_by_name(search_query), 1.0)]
        except ValueError:
            return []


class KnowledgeBase(object):
    object_storage_class = ObjectStorage

    def __init__(self, **kwargs):
        self._classes = {}
        for class_name, class_path in kwargs.items():
            self._classes[class_name.upper()] = self.create_class_storage(class_path, class_name)

    @property
    def supported_classes(self):
        return list(self._classes.keys())

    def create_class_storage(self, class_path, class_name):
        return self.object_storage_class(class_path, class_name)

    def get_class_storage(self, class_name):
        return self._classes[class_name.upper()]

    def get_object(self, class_name, object_id):
        return self.get_class_storage(class_name).get(object_id)

    def search(self, class_name, search_query):
        return self.get_class_storage(class_name).search(search_query)
