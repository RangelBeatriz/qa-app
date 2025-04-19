// static/script.js

document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const qaForm = document.getElementById("qaForm");
  
    uploadForm.onsubmit = async (e) => {
      e.preventDefault();
      const formData = new FormData(uploadForm);
      const res = await fetch("/upload/", {
        method: "POST",
        body: formData,
      });
      const json = await res.json();
      document.getElementById("uploadResult").innerText = "PDF carregado: " + json.filename;
    };
  
    qaForm.onsubmit = async (e) => {
      e.preventDefault();
      const question = document.getElementById("question").value;
      const res = await fetch("/ask/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question }),
      });
      const json = await res.json();
      document.getElementById("answerResult").innerText = "Resposta: " + json.answer;
    };
  });