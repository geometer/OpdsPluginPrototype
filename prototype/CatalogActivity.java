/*
 * This code is in the public domain.
 */

package %(PACKAGE)s.fbreader.plugin.opds;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.*;
import android.net.Uri;
import android.os.Bundle;

public class CatalogActivity extends Activity {
	@Override
	public void onCreate(Bundle bundle) {
		super.onCreate(bundle);
		try {
			startActivity(new Intent(
				"android.fbreader.action.OPEN_NETWORK_CATALOG",
				Uri.parse(new CatalogInfo().url())
			)
				.putExtra("SingleCatalog", true)
				.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK)
			);
			finish();
		} catch (ActivityNotFoundException e) {
			final DialogInterface.OnClickListener listener =
				new DialogInterface.OnClickListener() {
					public void onClick(DialogInterface dialog, int which) {
						if (which == DialogInterface.BUTTON_POSITIVE) {
							try {
								openUrl("market://details?id=org.geometerplus.zlibrary.ui.android");
							} catch (ActivityNotFoundException e) {
								openUrl("http://fbreader.org/FBReaderJ/");
							}
						}
						finish();
					}
				};
			new AlertDialog.Builder(this)
				.setTitle(R.string.missing_fbreader_dialog_title)
				.setMessage(R.string.missing_fbreader_dialog_message)
				.setIcon(0)
				.setPositiveButton(android.R.string.ok, listener)
				.setNegativeButton(android.R.string.cancel, listener)
				.create()
				.show();
		}
	}

	private void openUrl(String url) {
		startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(url)));
	}
}
