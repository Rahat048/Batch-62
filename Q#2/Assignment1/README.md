# Assignment: Understanding OpenAI Chat Completion API Parameters

## **Objective**

This assignment is designed to deepen understanding of the parameters used with the OpenAI Chat Completion API. Below is an explanation of the terms and parameters in my own words:

---

## **Terms/Parameters**

### **Model**

- Specifies the OpenAI model to use for generating responses.
- Different models have varying capabilities and accuracy.

---

### **Max Completion Tokens**

- Sets the maximum number of tokens the model can generate in the response.
- Tokens are chunks of words or characters.
- For example, `max_tokens=50` limits the response to approximately 50 tokens, helping control output length and resource usage.

---

### **n**

- Determines the number of completions (responses) generated for a single prompt.
- Example: If `n=3`, the API returns three distinct responses for the same input.

---

### **Tools**

- Refers to external integrations or functionalities available to the model during execution.

---

### **Messages**

- This is the conversation history between the user and the AI.
- Each message has two parts:
  1. **Role**: Who sent it (e.g., `"user"`, `"assistant"`, or `"system"`).
  2. **Content**: The actual text of the message.
- It helps the AI understand the context of the conversation.

---

### **Stream**

- When turned on (`true`), the AI sends the response piece by piece in real-time.
- This lets you see the answer as it is being created instead of waiting for the whole response.

---

### **Temperature**

- Controls how creative or random the AI’s responses are.
  - **Low value (e.g., 0.2)**: The AI gives more focused and predictable answers.
  - **High value (e.g., 1.0)**: The AI gives more varied and creative responses.

---

### **Top_p**

- Decides how many response options the AI considers when picking the next word.
  - **Top_p = 1.0**: Considers all possible words (more creative).
  - **Top_p = 0.9**: Focuses only on the top 90% most likely words (more focused and relevant).
