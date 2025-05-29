# Pre-Marketing Template Generator

This program helps marketers in Malaysia create comprehensive pre-marketing templates for their products. It generates structured content including product information, customer avatars, and marketing offers.

## Features

- Interactive input for product details
- Creation of 3 detailed customer avatars
- Generation of marketing offers for each avatar
- Automatic saving of templates in JSON format
- Support for Bahasa Malaysia content

## Requirements

- Python 3.6 or higher

## How to Use

1. Run the program:
   ```bash
   python premarketing_generator.py
   ```

2. Follow the prompts to enter:
   - Product information (brand name, problem, solution, etc.)
   - Details for 3 customer avatars
   - Marketing offers for each avatar

3. The program will save your template as a JSON file with a timestamp in the filename.

## Template Structure

The generated template includes:

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
- Optional creative suggestions

## Output

The program generates a JSON file named `premarketing_template_YYYYMMDD_HHMMSS.json` containing all the entered information in a structured format. 