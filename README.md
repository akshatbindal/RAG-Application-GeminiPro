# RAG-based Query Response System with Streamlit

This project is a Streamlit-based application that allows users to upload PDF files, create ChromaDB vectors, and query these vectors to get customized responses. The responses are generated using Google's Generative AI (Gemini) based on relevant passages retrieved from the ChromaDB vectors.

## Features

- Upload a PDF file and create a ChromaDB vector with a user-defined name.
- Query the created ChromaDB vector to get customized responses based on the content of the PDF.
- Simple and user-friendly interface powered by Streamlit.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/rag-query-response-system.git
    cd rag-query-response-system
    ```

2. **Create a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root directory and add your Gemini API key:
    ```env
    GEMINI_API_KEY=your_gemini_api_key
    ```

## Usage

1. **Run the Streamlit app**:
    ```bash
    streamlit run app.py
    ```

2. **Upload a PDF and Create ChromaDB Vector**:
    - Go to the sidebar in the Streamlit app.
    - Upload a PDF file.
    - Enter a name for the ChromaDB collection.
    - Click on "Create ChromaDB Vector".

3. **Query the ChromaDB Vector**:
    - Enter your query in the text input field.
    - Click on "Get Answer".
    - The app will retrieve relevant passages from the ChromaDB vector and generate a response based on the query.

## Dependencies

- [Streamlit](https://streamlit.io/)
- [ChromaDB](https://github.com/chroma-core/chroma)
- [Google Generative AI](https://cloud.google.com/ai-platform/generative-ai)
- Other dependencies are listed in `requirements.txt`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the Apache License.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [ChromaDB](https://github.com/chroma-core/chroma)
- [Google Generative AI](https://cloud.google.com/ai-platform/generative-ai)

