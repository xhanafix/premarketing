# Pre-Marketing Template Generator

A powerful tool for Malaysian marketers to create comprehensive pre-marketing templates using AI. This tool generates structured content including product information, customer avatars, and marketing offers in Bahasa Malaysia.

## Features

- 🤖 AI-powered content generation using OpenRouter API
- 📝 Interactive input for product details
- 👥 Creation of 3 detailed customer avatars
- 💡 Generation of marketing offers for each avatar
- 📄 Automatic PDF generation with professional formatting
- 🇲🇾 Support for Bahasa Malaysia content
- 🔒 Secure API key management using environment variables

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/xhanafix/premarketing.git
   cd premarketing
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## API Setup

1. Get your API key from [OpenRouter](https://openrouter.ai/)
2. Create a `.env` file in the project root:
   ```
   OPENROUTER_API_KEY=your_api_key_here
   ```
   Or run the program and enter your API key when prompted.

## Usage

1. Run the program:
   ```bash
   python premarketing_generator.py
   ```

2. Follow the prompts to enter:
   - Brand name
   - Product name
   - Product description

3. The program will automatically generate:
   - Product information
   - Customer avatars
   - Marketing offers

4. A PDF file will be generated with the format: `premarketing_template_YYYYMMDD_HHMMSS.pdf`

## Template Structure

### PART 1 – PRODUK
- Problem and solution
- Product mechanism/ingredients
- Usage instructions

### PART 2 – AVATAR & PERSONA
For each avatar:
- Name, age, occupation
- Demographics
- User story
- Daily routine
- Goals and frustrations

### PART 3 – OFFER
For each avatar:
- 10 headline ideas
- 5 intro paragraphs
- 3 product promises
- Creative suggestions for ads

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [xhanafix](https://github.com/xhanafix)

## Acknowledgments

- OpenRouter API for AI content generation
- ReportLab for PDF generation 