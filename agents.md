# Sproutt Demo App Build Instructions

## Goals and Non-Goals

### Goals
- Create a lightweight, read-only "tour" of Sproutt functionality
- Demonstrate core modules: Sales, Purchasing, Operations, Reports, Prospecting, AI Parts Analysis, Price Lists, Customer Portal
- Highlight key features: AI data extraction, email connectivity, lead generation based on existing customer base, customer-facing modules (price lists, order status)
- Use realistic but fake demo data (boring company, realistic numbers)
- Match Sproutt's UI/UX patterns and branding
- Be safe: no POST routes, no DB writes, no external API calls, no real data exposure
- Show AI features as pre-rendered examples only

### Non-Goals
- Full functionality of any module
- User authentication or session management
- Database integration or data persistence
- Lead generation or customer data collection
- External integrations (email, APIs, etc.)
- Real-time features or dynamic interactions

## Safety Constraints
- **NO POST routes**: All endpoints must be GET only
- **NO database**: Use static JSON files for demo data
- **NO external calls**: No OpenAI, HubSpot, email APIs, etc.
- **NO uploads**: No file handling or storage
- **NO actions**: No forms, buttons that do anything, or state changes
- **Read-only**: All pages show static, pre-generated content

## Recommended File Structure
```
sproutt-demo/
├── app.py                    # Flask app factory
├── demo_data.py              # Fake demo data generation
├── demo_data.json            # Static JSON data (generated)
├── requirements.txt          # Dependencies
├── static/
│   ├── css/
│   │   ├── lumen.css         # Bootstrap theme (copy from Sproutt)
│   │   ├── solid-colors.css  # Sproutt branding colors (copy)
│   │   └── styles.css        # Custom styles (copy from Sproutt)
│   ├── js/
│   │   └── scripts.js        # Minimal JS (copy if needed)
│   └── logo.png              # Sproutt logo (copy)
└── templates/
    ├── base_demo.html        # Demo base template (extend Sproutt base)
    └── demo/
        ├── index.html        # Landing page with module cards
        ├── sales.html        # Sales Orders demo
        ├── purchasing.html   # Purchase Orders demo
        ├── operations.html   # Projects demo
        ├── reports.html      # Dashboard/Reports demo
        ├── prospecting.html  # Customer prospecting demo
        ├── ai_analysis.html  # AI Parts Analysis demo
        ├── price_lists.html  # Customer-facing price lists demo
        └── portal.html       # Customer portal demo
```

## Step-by-Step Implementation Plan

### 1. Setup Project Structure
- Create Flask app.py with minimal config
- Copy branding assets from Sproutt static folder:
  - solid-colors.css
  - lumen.css
  - styles.css (relevant parts)
  - logo.png
- Create base_demo.html template extending Sproutt patterns

### 2. Generate Demo Data
- Create demo_data.py with functions to generate fake data
- Focus on believable, boring company scenarios:
  - Company: "ABC Manufacturing Ltd"
  - Parts: Standard industrial components (bearings, motors, etc.)
  - Customers: Generic B2B companies
  - Realistic quantities, prices, dates
- Generate JSON files for each module's demo data

### 3. Implement Demo Routes
- `/demo` - Landing page with module overview cards
- `/demo/sales` - Show fake sales orders table/list
- `/demo/purchasing` - Show fake purchase orders
- `/demo/operations` - Show fake projects/tasks
- `/demo/reports` - Show fake dashboard with charts/tables
- `/demo/prospecting` - Show fake customer prospecting with AI insights
- `/demo/ai-analysis` - Show fake AI parts analysis with suggestions
- `/demo/price-lists` - Show customer-facing price lists
- `/demo/portal` - Show customer portal with order status

### 4. Create Demo Templates
- Use Sproutt's table/list patterns from templates
- Add prominent "DEMO / FAKE DATA" banners
- Make all links inactive or self-referential
- Include realistic-looking data tables and forms (disabled)

### 5. Style Consistency
- Copy Sproutt's sidebar navigation structure (simplified)
- Use same color scheme from solid-colors.css
- Match typography and spacing
- Include logo and branding elements

### 6. Demo Data Guidelines
- **Company**: "ABC Manufacturing Ltd" - produces industrial equipment
- **Parts**: Common industrial parts with realistic pricing (€50-5000)
- **Customers**: 5-10 generic companies (TechCorp, Industrial Ltd, etc.)
- **Quantities**: Realistic (1-100 units)
- **Dates**: Recent past and near future
- **AI Features**: Show pre-written examples of AI suggestions/analysis
- **Status**: Mix of active, completed, pending items

### 7. Key Features to Highlight in Demo
- **AI Data Extraction**: Show intelligent parts analysis with supplier suggestions, cost optimization, and sourcing recommendations
- **Email Connectivity**: Demonstrate email integration patterns (mailbox sync, contact extraction from emails)
- **Lead Generation**: Display prospecting tools that target customers based on existing customer base, industry analysis, and automated insights
- **Customer-Facing Modules**: Include public price lists and customer portal features for order status tracking

### 8. Language Guidelines
- **Avoid Buzz Phrases**: Don't start descriptions with phrases like "AI-driven", "AI-powered", or "cutting-edge" as these are overused buzzwords
- **Focus on Benefits**: Emphasize what the features do rather than labeling them with trendy terms
- **Professional Tone**: Use business-appropriate language that highlights practical value and reliability

## Definition of Done Checklist
- [ ] Flask app runs without errors
- [ ] All routes are GET-only
- [ ] No database connections or external APIs
- [ ] Demo banner visible on all pages
- [ ] Realistic fake data in all modules
- [ ] UI matches Sproutt branding/colors
- [ ] Navigation works between demo pages
- [ ] Tables show sortable/filterable demo data
- [ ] No interactive elements (forms, buttons) function
- [ ] AI features shown as static examples
- [ ] Code is minimal and maintainable

## Notes on Isolated/Reversible Changes
- All demo code in separate files (demo_data.py, demo routes)
- No modifications to existing Sproutt code
- Clear separation between real app and demo
- Easy to remove demo routes by commenting out blueprint registration
- Static assets copied, not symlinked, for independence
