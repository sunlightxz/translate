from googletrans import Translator
import polib


def translate_po(input_po_file, output_po_file, target_lang):
    try:
        # Initialize translator
        translator = Translator()

        # Load the .po file
        po = polib.pofile(input_po_file)

        # Translate each entry in the .po file
        translations_successful = 0
        translations_failed = 0

        for entry in po:
            if not entry.obsolete:
                try:
                    # Translate the msgid text to the target language
                    translated_text = translator.translate(entry.msgid, src='en', dest=target_lang).text
                    entry.msgstr = translated_text
                    translations_successful += 1
                except Exception as e:
                    print(f"Error translating {entry.msgid}: {str(e)}")
                    translations_failed += 1

        # Save translated .po file
        po.save(output_po_file)

        print(f"Translation complete. Translated {translations_successful} entries successfully. {translations_failed} entries failed.")

    except IOError as e:
        print(f"Error loading or parsing .po file: {str(e)}")



if __name__ == "__main__":
    input_po_file = "/Users/asmac/Documents/script/translate/ar.po"
    output_po_file = "/Users/asmac/Documents/script/translate/translated_ar.po"
    target_lang = "ar"

    translate_po(input_po_file, output_po_file, target_lang)
