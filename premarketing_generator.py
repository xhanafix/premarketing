import json
from datetime import datetime
from typing import Dict, List
import os
from dotenv import load_dotenv
import requests
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

class PreMarketingGenerator:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Get API key from environment variable
        self.api_key = os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            print("Warning: OPENROUTER_API_KEY not found in environment variables")
        
        self.template = {
            "PART 1 – PRODUK": {
                "Problem & Solution": "",
                "Mechanism": "",
                "Usage Instructions": ""
            },
            "PART 2 – AVATAR & PERSONA": [],
            "PART 3 – OFFER": []
        }
        
        # OpenRouter API configuration
        self.api_url = "https://openrouter.ai/api/v1/chat/completions"
        self.model = "deepseek/deepseek-chat-v3-0324:free"

        # PDF styles
        self.styles = getSampleStyleSheet()
        
        # Custom styles with unique names
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            fontName='Helvetica-Bold',
            fontSize=24,
            leading=28,
            alignment=TA_CENTER,
            spaceAfter=30,
            textColor=colors.HexColor('#2C3E50')
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomMainHeading',
            fontName='Helvetica-Bold',
            fontSize=20,
            leading=24,
            spaceBefore=20,
            spaceAfter=15,
            textColor=colors.HexColor('#2C3E50')
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomSubHeading',
            fontName='Helvetica-Bold',
            fontSize=16,
            leading=20,
            spaceBefore=15,
            spaceAfter=10,
            textColor=colors.HexColor('#34495E')
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomContent',
            fontName='Helvetica',
            fontSize=12,
            leading=16,
            spaceBefore=6,
            spaceAfter=6,
            textColor=colors.HexColor('#2C3E50')
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomAvatar',
            fontName='Helvetica',
            fontSize=12,
            leading=16,
            leftIndent=20,
            spaceBefore=10,
            spaceAfter=10,
            textColor=colors.HexColor('#2C3E50')
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomOffer',
            fontName='Helvetica',
            fontSize=12,
            leading=16,
            leftIndent=20,
            spaceBefore=10,
            spaceAfter=10,
            textColor=colors.HexColor('#2C3E50')
        ))

    def configure_api_key(self):
        """Configure API key"""
        print("\n=== OpenRouter API Configuration ===")
        api_key = input("Enter your OpenRouter API key (or press Enter to skip): ").strip()
        
        if api_key:
            # Save to .env file
            with open('.env', 'w') as f:
                f.write(f'OPENROUTER_API_KEY={api_key}')
            self.api_key = api_key
            print("API key saved successfully!")
        else:
            print("No API key provided. Some features may be limited.")

    def generate_ai_content(self, prompt: str) -> str:
        """Generate content using OpenRouter API"""
        if not self.api_key:
            return "API key not configured. Please set up your OpenRouter API key."

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://github.com/yourusername/premarketing-generator",
            "X-Title": "Pre-Marketing Generator"
        }

        data = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a professional marketing strategist specializing in the Malaysian market. Provide responses in Bahasa Malaysia."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            return f"Error generating content: {str(e)}"

    def get_product_info(self) -> Dict:
        """Get basic product information from user input"""
        print("\n=== PART 1: PRODUK INFORMATION ===")
        brand_name = input("Enter brand name: ")
        product_name = input("Enter product name: ")
        product_description = input("Enter detailed product description: ")

        # Generate complete product information using AI
        prompt = f"""Based on this product information:
        Brand: {brand_name}
        Product: {product_name}
        Description: {product_description}

        Please generate a complete pre-marketing template in Bahasa Malaysia with the following sections:

        PART 1 – PRODUK:
        1. Problem & Solution (What problem does this product solve and how?)
        2. Mechanism (How does it work? Include ingredients/technology if applicable)
        3. Usage Instructions (How to use the product)

        Format the response in clear sections with headings."""

        print("\nGenerating product information...")
        product_info = self.generate_ai_content(prompt)
        print("\nGenerated Product Information:")
        print(product_info)
        
        # Parse the AI response into sections
        sections = product_info.split('\n\n')
        return {
            "brand_name": brand_name,
            "product_name": product_name,
            "product_description": product_description,
            "generated_content": product_info
        }

    def generate_avatars(self, product_info: Dict) -> List[Dict]:
        """Generate customer avatars using AI"""
        print("\nGenerating customer avatars...")
        
        prompt = f"""Based on this product:
        Brand: {product_info['brand_name']}
        Product: {product_info['product_name']}
        Description: {product_info['product_description']}

        Create 3 detailed customer avatars in Bahasa Malaysia. For each avatar include:
        - Name
        - Age
        - Job
        - Demographics (location, income level)
        - User story (how they encounter the product)
        - Daily routine
        - Goals
        - Frustrations

        Format each avatar as a separate section with clear headings."""

        avatars_content = self.generate_ai_content(prompt)
        print("\nGenerated Customer Avatars:")
        print(avatars_content)
        
        # Split the content into individual avatars
        avatar_sections = avatars_content.split('\n\n\n')
        return [{"content": section.strip()} for section in avatar_sections if section.strip()]

    def generate_offers(self, product_info: Dict, avatars: List[Dict]) -> List[Dict]:
        """Generate marketing offers for each avatar using AI"""
        print("\nGenerating marketing offers...")
        
        offers = []
        for avatar in avatars:
            prompt = f"""Based on this product and customer avatar:
            Product: {product_info['product_name']}
            Description: {product_info['product_description']}
            Avatar: {avatar['content']}

            Create a complete marketing offer in Bahasa Malaysia including:
            1. 10 compelling headlines
            2. 5 engaging intro paragraphs
            3. 3 powerful product promises
            4. Creative suggestions for ads

            Format the response in clear sections with headings."""

            offer_content = self.generate_ai_content(prompt)
            print(f"\nGenerated Offer for Avatar:")
            print(offer_content)
            
            offers.append({"content": offer_content})
        
        return offers

    def generate_template(self):
        """Generate the complete pre-marketing template"""
        # Get basic product information
        product_info = self.get_product_info()
        
        # Generate avatars
        avatars = self.generate_avatars(product_info)
        
        # Generate offers for each avatar
        offers = self.generate_offers(product_info, avatars)
        
        # Update template
        self.template["PART 1 – PRODUK"] = {
            "Problem & Solution": product_info['generated_content'],
            "Mechanism": "",
            "Usage Instructions": ""
        }
        self.template["PART 2 – AVATAR & PERSONA"] = avatars
        self.template["PART 3 – OFFER"] = offers

    def format_section(self, content: str) -> List[str]:
        """Format content into paragraphs with proper spacing"""
        # Split content into paragraphs and remove empty lines
        paragraphs = [p.strip() for p in content.split('\n') if p.strip()]
        return paragraphs

    def create_section_break(self):
        """Create a visual section break"""
        return [
            Spacer(1, 0.2*inch),
            Paragraph("•" * 50, self.styles['CustomContent']),
            Spacer(1, 0.2*inch)
        ]

    def save_template(self):
        """Save the template to a PDF file"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"premarketing_template_{timestamp}.pdf"
        
        # Create PDF document with wider margins
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=1*inch,
            leftMargin=1*inch,
            topMargin=1*inch,
            bottomMargin=1*inch
        )
        
        # Build PDF content
        story = []
        
        # Title
        story.append(Paragraph("PRE-MARKETING TEMPLATE", self.styles['CustomTitle']))
        story.append(Spacer(1, 0.5*inch))
        
        # PART 1 – PRODUK
        story.append(Paragraph("PART 1 – PRODUK", self.styles['CustomMainHeading']))
        story.append(Spacer(1, 0.2*inch))
        
        # Add product information
        product_content = self.template["PART 1 – PRODUK"]["Problem & Solution"]
        for paragraph in self.format_section(product_content):
            story.append(Paragraph(paragraph, self.styles['CustomContent']))
        
        story.extend(self.create_section_break())
        
        # PART 2 – AVATAR & PERSONA
        story.append(Paragraph("PART 2 – AVATAR & PERSONA", self.styles['CustomMainHeading']))
        story.append(Spacer(1, 0.2*inch))
        
        # Add avatars
        for i, avatar in enumerate(self.template["PART 2 – AVATAR & PERSONA"], 1):
            story.append(Paragraph(f"Avatar {i}", self.styles['CustomSubHeading']))
            for paragraph in self.format_section(avatar['content']):
                story.append(Paragraph(paragraph, self.styles['CustomAvatar']))
            story.append(Spacer(1, 0.2*inch))
        
        story.extend(self.create_section_break())
        story.append(PageBreak())
        
        # PART 3 – OFFER
        story.append(Paragraph("PART 3 – OFFER", self.styles['CustomMainHeading']))
        story.append(Spacer(1, 0.2*inch))
        
        # Add offers
        for i, offer in enumerate(self.template["PART 3 – OFFER"], 1):
            story.append(Paragraph(f"Offer for Avatar {i}", self.styles['CustomSubHeading']))
            for paragraph in self.format_section(offer['content']):
                story.append(Paragraph(paragraph, self.styles['CustomOffer']))
            story.append(Spacer(1, 0.2*inch))
        
        # Build PDF
        doc.build(story)
        print(f"\nTemplate saved to {filename}")

def main():
    print("Welcome to Pre-Marketing Template Generator")
    print("This program will help you create a comprehensive pre-marketing template.")
    print("You only need to provide the brand name, product name, and product description.")
    print("The AI will generate the rest of the content in Bahasa Malaysia.")
    
    generator = PreMarketingGenerator()
    
    # Configure API key if not already set
    if not generator.api_key:
        generator.configure_api_key()
    
    generator.generate_template()
    generator.save_template()

if __name__ == "__main__":
    main() 