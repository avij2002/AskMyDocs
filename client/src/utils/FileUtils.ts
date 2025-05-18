const validatePDFFile = (file: File, callback?: () => void): boolean => {
  const isPDF = file?.type === "application/pdf" || file.name.endsWith(".pdf");
  if (!isPDF) {
    if (callback) {
      callback();
    }
    return false;
  }
  return true;
};

export { validatePDFFile };
