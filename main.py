import os
import json
import argparse
import torch
import whisper
from pathlib import Path


def find_media_files(directory, extensions={".mp3", ".mp4", ".mov", ".wmv", ".avi"}):
    # find all media files in the given directory
    media_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                media_files.append(os.path.join(root, file))
    return media_files


def transcribe_media(file_path, model):
    # Transcribe a given media file using Whisper
    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)
    return result["text"]


def save_transcription(file_path, transcription, output_dir):
    # Save transcription in a JSON
    output_dir = Path(output_dir) if output_dir else Path(file_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / (Path(file_path).stem + ".json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump({"file": file_path, "transcription": transcription}, f, indent=4)

    print(f"Saved transcription: {output_file}")


def main(input_folder, output_folder=None):
    # Main function to find, transcribe, and save results
    model = whisper.load_model("tiny")  # Load the smallest Whisper model
    media_files = find_media_files(input_folder)

    if not media_files:
        print("No media files found.")
        return

    for media_file in media_files:
        transcription = transcribe_media(media_file, model)
        save_transcription(media_file, transcription, output_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe media files in a directory using Whisper.")
    parser.add_argument("input_folder", help="Path to the input folder containing media files.")
    parser.add_argument("--output_folder", help="Optional path to save transcriptions.", default=None)

    args = parser.parse_args()
    main(args.input_folder, args.output_folder)
