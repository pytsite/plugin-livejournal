"""PytSite LiveJournal Plugin
"""
from pytsite import plugman as _plugman

if _plugman.is_installed(__name__):
    # Public API
    from ._session import Session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'
