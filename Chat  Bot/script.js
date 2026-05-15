const GEMINI_API_KEY = "AIzaSyAXiKXsyIH_ljK-osCte1Nkp7uh4dHKkis";

async function sendMessage() {

  const input = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");

  const userText = input.value;

  if (userText === "") return;

  // User message
  const userMessage = document.createElement("div");
  userMessage.classList.add("user-message");
  userMessage.innerText = userText;

  chatBox.appendChild(userMessage);

  input.value = "";

  // API Call
  const response = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        contents: [
          {
            parts: [
              {
                text: userText,
              },
            ],
          },
        ],
      }),
    }
  );

  const data = await response.json();

  const botReply =
    data.candidates[0].content.parts[0].text;

  // Bot message
  const botMessage = document.createElement("div");
  botMessage.classList.add("bot-message");
  botMessage.innerText = botReply;

  chatBox.appendChild(botMessage);

  chatBox.scrollTop = chatBox.scrollHeight;
}