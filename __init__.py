"""PytSite LiveJournal Package.
"""
# Public API
from ._session import Session

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    """Init wrapper.
    """
    from pytsite import lang, assetman
    from ._content_export import Driver as ContentExportDriver

    # Resources
    lang.register_package(__name__, alias='livejournal')
    assetman.register_package(__name__, alias='livejournal')

    # Content export driver
    try:
        from plugins import content_export
        content_export.register_driver(ContentExportDriver())
    except ImportError as e:
        raise RuntimeError("Required plugin is not found: {}".format(e))


_init()
