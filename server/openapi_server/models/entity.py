# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.user import User
from openapi_server import util

# from openapi_server.models.user import User  # noqa: E501


class Entity(Model):
    """
    NOTE: This class is auto generated by OpenAPI Generator
    (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created_by=None, created_at=None, updated_by=None, updated_at=None):  # noqa: E501
        """Entity - a model defined in OpenAPI

        :param id: The id of this Entity.  # noqa: E501
        :type id: int
        :param created_by: The created_by of this Entity.  # noqa: E501
        :type created_by: User
        :param created_at: The created_at of this Entity.  # noqa: E501
        :type created_at: datetime
        :param updated_by: The updated_by of this Entity.  # noqa: E501
        :type updated_by: User
        :param updated_at: The updated_at of this Entity.  # noqa: E501
        :type updated_at: datetime
        """
        self.openapi_types = {
            'id': int,
            'created_by': User,
            'created_at': datetime,
            'updated_by': User,
            'updated_at': datetime
        }

        self.attribute_map = {
            'id': 'id',
            'created_by': 'createdBy',
            'created_at': 'createdAt',
            'updated_by': 'updatedBy',
            'updated_at': 'updatedAt'
        }

        self._id = id
        self._created_by = created_by
        self._created_at = created_at
        self._updated_by = updated_by
        self._updated_at = updated_at

    @classmethod
    def from_dict(cls, dikt) -> 'Entity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Entity of this Entity.  # noqa: E501
        :rtype: Entity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Entity.

        ID  # noqa: E501

        :return: The id of this Entity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Entity.

        ID  # noqa: E501

        :param id: The id of this Entity.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Entity.


        :return: The created_by of this Entity.
        :rtype: User
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Entity.


        :param created_by: The created_by of this Entity.
        :type created_by: User
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this Entity.

        When the entity has been created  # noqa: E501

        :return: The created_at of this Entity.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Entity.

        When the entity has been created  # noqa: E501

        :param created_at: The created_at of this Entity.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_by(self):
        """Gets the updated_by of this Entity.


        :return: The updated_by of this Entity.
        :rtype: User
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this Entity.


        :param updated_by: The updated_by of this Entity.
        :type updated_by: User
        """

        self._updated_by = updated_by

    @property
    def updated_at(self):
        """Gets the updated_at of this Entity.

        When the entity has been updated  # noqa: E501

        :return: The updated_at of this Entity.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Entity.

        When the entity has been updated  # noqa: E501

        :param updated_at: The updated_at of this Entity.
        :type updated_at: datetime
        """

        self._updated_at = updated_at
