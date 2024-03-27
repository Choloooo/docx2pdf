function handleFileUpload(event) {
    const file = event.target.files[0];
  
    // Check if a file is selected
    if (!file) {
      alert("Please select a file to convert.");
      return;
    }
  
    // Validate file type (DOCX only)
    const validExtensions = ["docx"];
    const extension = file.name.split('.').pop().toLowerCase();
    if (!validExtensions.includes(extension)) {
      alert("Only .docx files are supported for conversion.");
      return;
    }
  
    // Create a FormData object to send the file to the server
    const formData = new FormData();
    formData.append("file", file);
  
    // Send an AJAX request to the server-side script
    fetch("/convert-to-pdf", {
      method: "POST",
      body: formData
    })
    .then(response => response.text())
    .then(data => {
      // Handle server response (e.g., display success message or download link)
      if (data === "success") {
        alert("File successfully converted to PDF!");
      } else {
        alert("Error during conversion: " + data);
      }
    })
    .catch(error => {
      alert("An error occurred: " + error);
    });
  }
  
  // Add event listener to the file input element
  const fileInput = document.getElementById('file-input');
  fileInput.addEventListener('change', handleFileUpload);
  