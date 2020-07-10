# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:23:07 2020

@author: twshere
"""

from PyQt5.QtGui import QColor
from enum import Enum

class Object(tuple):
    def __init__(self, content=None):
        tuple.__init__(content or ())
    def __getattr__(self, s):
        return Object((*self, s))
    def __repr__(self):
        return '.'.join(self)            


_global_style_ids = {}
_global_id_names = {}
def enrich_reflection(cls):
    for i, style in enumerate(cls):
        _global_style_ids[style] = i
        _global_id_names[i] = style.name
    
    @property
    def style_id(self):
        return _global_style_ids[self]
    
    @staticmethod
    def name_of_style_id(id, default):
        return _global_id_names.get(id, default)
    
    cls.style_id = style_id
    cls.name_of_style_id = name_of_style_id
    return cls

def color(s):
    if isinstance(s, str):
        return QColor('#ff' + s.lower()[1:])
    raise TypeError(s, type(s))

@enrich_reflection
class Theme(Enum):
    Comment = [color("#EE6850")]
    Literal = [color("#66CD00")]
    Keyword = [color("#CD3278")]
    String = [color("#D15FEE")]
    Var = [color("#1874CD")]
    Pattern = [color("#473C8B")]
    Call = [color("#6959CD")]
    Type = [color("#00688B")]
    Error = [color("#FF34B3")]
    
    @property
    def style_id(self) -> int:
        return NotImplementedError

    
    def name_of_style_id(self, id, default) -> str:
        return NotImplementedError

print(Theme.Comment.style_id)