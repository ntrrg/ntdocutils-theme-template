"""{{ Name }} theme for NtDocutils."""

__docformat__ = "reStructuredText"

from os import path
import shutil

from ntdocutils.writer import Writer as NtDocutilsWriter


class Writer(NtDocutilsWriter):
    """Creates a {{ Name }} theme writer."""

    theme_path = path.dirname(path.abspath(__file__))
    theme = path.basename(theme_path)

    def __init__(self, server):
        if not server:
            server = "{{ Server }}"

        NtDocutilsWriter.__init__(self, server)

        self.docutils_argv["template"] = path.join(
            self.theme_path,
            "template.html"
        )

    def assets(self):
        assets = {}

        # Templates for assets
        stylesheet = "<link rel='stylesheet' href='{}' />"

        # Target in template.html
        assets["styles"] = stylesheet.format(
            "{server}/css/styles.css"
        ).format(server=server)

        return assets

    def offline_mode(self, destination):
        dest_dir = path.join(
            path.dirname(path.abspath(destination)),
            self.theme
        )

        css_dest_dir = path.join(dest_dir, "css")

        # Delete theme folder if exists
        shutil.rmtree(dest_dir, ignore_errors=True)

        # Copy assets in ``destination`` parent folder
        shutil.copytree(path.join(self.theme_path, "css"), css_dest_dir)

