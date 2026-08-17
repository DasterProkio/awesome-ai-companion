# Web index

Source of the searchable web version at <https://lutopia.app/companion/>.

Single self-contained HTML file — no build step, no dependencies. Deploy by
copying `index.html` to the web root.

Includes canonical URL, Open Graph and Twitter card metadata, JSON-LD
(`CollectionPage` + `ItemList` + `BreadcrumbList`), and a `<noscript>` static
index so the full entry list is reachable without JavaScript.
