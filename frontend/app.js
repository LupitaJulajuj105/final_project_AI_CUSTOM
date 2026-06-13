const askForm = document.querySelector("#ask-form");
const contextForm = document.querySelector("#context-form");
const answerOutput = document.querySelector("#answer-output");
const contextOutput = document.querySelector("#context-output");

const API_BASE_URL = "http://127.0.0.1:8000";

function getUserId() {
  return document.querySelector("#user-id").value || "student-01";
}

askForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(askForm);
  const payload = {
    user_id: formData.get("user_id"),
    question: formData.get("question"),
  };

  answerOutput.textContent = "Consultando...";

  try {
    const response = await fetch(`${API_BASE_URL}/api/ask`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const result = await response.json();
    answerOutput.textContent = JSON.stringify(result, null, 2);
    await loadContext(payload.user_id);
  } catch (error) {
    answerOutput.textContent = `No se pudo conectar con el backend: ${error.message}`;
  }
});

contextForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(contextForm);
  const userId = getUserId();
  const payload = {
    user_id: userId,
    key: formData.get("key"),
    value: formData.get("value"),
  };

  try {
    const response = await fetch(`${API_BASE_URL}/api/context`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const result = await response.json();
    await loadContext(userId);
  } catch (error) {
    contextOutput.textContent = `Error al guardar contexto: ${error.message}`;
  }
});

async function loadContext(userId) {
  try {
    const response = await fetch(`${API_BASE_URL}/api/context?user_id=${encodeURIComponent(userId)}`);
    const result = await response.json();
    contextOutput.textContent = JSON.stringify(result, null, 2);
  } catch (error) {
    contextOutput.textContent = "El modulo CAG aun no esta disponible.";
  }
}

loadContext(getUserId());
