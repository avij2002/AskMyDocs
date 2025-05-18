import React, { useState, useRef } from "react";
import FileUploadIcon from "../assets/FileUploadIcon";
import { Button } from "@/components/ui/button";
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";
import { validatePDFFile } from "@/utils/FileUtils";

const FileUploader = () => {
  const [isDraggingFileOver, setIsDraggingFileOver] = useState<boolean>(false);
  const [uploadedFile, setUploadedFile] = useState<File | null>(null);
  const [showInvalidFileTypeDialog, setShowInvalidFileTypeDialog] =
    useState<boolean>(false);

  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleDropZoneClick = () => {
    console.log("dropZone clicked");
    fileInputRef.current?.click();
  };

  const handleDragOverDropZone = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    console.log(event);
    if (!isDraggingFileOver) {
      setIsDraggingFileOver(true);
    }
    console.log("drag");
  };

  const validatePDFFileCallback = () => {
    setShowInvalidFileTypeDialog(true);
  };

  const handleFileDrop = (event: React.DragEvent<HTMLDivElement>) => {
    event.preventDefault();
    const file = event.dataTransfer.files?.[0];
    if (file && validatePDFFile(file, validatePDFFileCallback)) {
      setUploadedFile(file);
    }
    setIsDraggingFileOver(false);
  };

  const handleFileSelect = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file && validatePDFFile(file, validatePDFFileCallback)) {
      setUploadedFile(file);
    }
  };

  return (
    <>
      <div className="h-1/2 w-1/2 bg-white flex justify-center items-center shadow-2xl rounded-2xl flex-col">
        <h3 className="font-sans">Upload a Document</h3>
        <div
          role="button"
          tabIndex={0}
          className={`border border-dotted rounded-2xl h-36 w-36 flex items-center justify-center transition-shadow duration-200 hover:shadow-xl hover:cursor-pointer ${
            isDraggingFileOver ? "transition-shadow duration-200 shadow-xl" : ""
          } `}
          onClick={handleDropZoneClick}
          onDragOver={handleDragOverDropZone}
          onDragLeave={() => {
            setIsDraggingFileOver(false);
          }}
          onDrop={handleFileDrop}
        >
          <div className="h-6 w-6">
            <FileUploadIcon />
          </div>{" "}
          <span>Choose a file</span>
        </div>
        {uploadedFile && <h4>File selected: {uploadedFile.name}</h4>}

        <Button className="cursor-pointer" disabled={!uploadedFile}>
          Upload the file
        </Button>
      </div>

      <Dialog
        open={showInvalidFileTypeDialog}
        onOpenChange={setShowInvalidFileTypeDialog}
      >
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Invalid File Type</DialogTitle>
            <DialogDescription>Please select a PDF File</DialogDescription>
          </DialogHeader>
        </DialogContent>
      </Dialog>

      <input
        type="file"
        className="hidden"
        onChange={handleFileSelect}
        ref={fileInputRef}
      />
    </>
  );
};
export default FileUploader;
