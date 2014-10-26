/*
 * This code is in the public domain.
 */

package %(PACKAGE)s.fbreader.plugin.opds;

import org.fbreader.plugin.opds.AbstractCatalogInfo;

public class CatalogInfo extends AbstractCatalogInfo {
	@Override
	protected String url() {
        return "%(URL)s";
	}
}
