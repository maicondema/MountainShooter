#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code.Const import WIN_WIDTH
from Code.background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
           case 'Free-Mountain':
              list_art = []
              for i in range(1, 7):
                  list_art.append(Background(f'Free-Mountain-0{i}', (0, 0)))
                  list_art.append(Background(f'Free-Mountain-0{i}', (WIN_WIDTH, 0)))

              return list_art



