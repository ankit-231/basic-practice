"""
With the exception of __name__, it is strongly recommended that you rely on __spec__ and its attributes instead of any of the other individual attributes listed in this subsection. Note that updating an attribute on __spec__ will not update the corresponding attribute on the module itself:

>>> import typing
>>> typing.__name__, typing.__spec__.name
('typing', 'typing')
>>> typing.__spec__.name = 'spelling'
>>> typing.__name__, typing.__spec__.name
('typing', 'spelling')
>>> typing.__name__ = 'keyboard_smashing'
>>> typing.__name__, typing.__spec__.name
('keyboard_smashing', 'spelling')
"""

import typing

print("typing.__name__, typing.__spec__.name:", (typing.__name__, typing.__spec__.name))
