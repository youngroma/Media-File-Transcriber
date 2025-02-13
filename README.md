# Media File Transcriber

This Python script processes a directory of media files by:

- **Folder Parsing**: Recursively scanning the provided folder (including subfolders) to locate any audio or video files.
- **Transcription**: Using OpenAI's Whisper package with the smallest available model to transcribe each media file.
- **Saving Results**: Storing each transcription in a structured format (JSON) alongside the original files or in a designated output folder.

## Requirements

Before running the script, ensure you have the required dependencies installed. You can install them using:

```bash
pip install -r requirements.txt
```

## Usage

Run the script from the command line:

```bash
python transcriber.py <input_folder> --output_folder <output_folder>
```

### Arguments

- `<input_folder>`: Path to the directory containing media files to transcribe.
- `--output_folder <output_folder>` (optional): Path to save the transcription results. If not provided, transcriptions will be saved alongside the original media files.

### Example

```bash
python transcriber.py ./media --output_folder ./transcriptions
```

## Supported Media Formats

The script scans for media files with the following extensions:

- `.mp3`
- `.mp4`
- `.mov`
- `.wmv`
- `.avi`

## How It Works

1. The script recursively finds media files in the given input folder.
2. It transcribes each media file using Whisper's `tiny` model.
3. Transcriptions are saved in a JSON format with the structure:
   ```json
   {
       "file": "path/to/media/file.mp3",
       "transcription": "Transcribed text here..."
   }
   ```

## Notes

- The script uses Whisper's **tiny** model for fast transcription. You can modify the script to use other models (`base`, `small`, `medium`, `large`) by changing:
  ```python
  model = whisper.load_model("tiny")
  ```

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

