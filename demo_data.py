import json
import random
from datetime import datetime, timedelta

def generate_demo_data():
    """Generate over-the-top fake demo data for all Sproutt modules"""

    # Generate sales data
    sales_orders = []
    total_sales_value = 0
    for i in range(50):
        value = random.randint(5000, 150000)
        total_sales_value += value
        sales_orders.append({
            'id': f'SO-{2026}-{i+1:03d}',
            'customer': random.choice(['TechCorp Ltd', 'Industrial Solutions GmbH', 'Manufacturing Inc', 'Global Parts Co', 'Precision Engineering Ltd']),
            'value': value,
            'status': random.choice(['Active', 'Pending', 'Completed', 'Shipped']),
            'date': (datetime.now() - timedelta(days=random.randint(0, 90))).strftime('%Y-%m-%d')
        })

    # Generate purchasing data
    purchase_orders = []
    total_purchase_value = 0
    for i in range(35):
        value = random.randint(3000, 80000)
        total_purchase_value += value
        purchase_orders.append({
            'id': f'PO-{2026}-{i+1:03d}',
            'supplier': random.choice(['Global Components', 'Industrial Parts Ltd', 'Precision Manufacturing', 'Quality Suppliers Inc']),
            'value': value,
            'status': random.choice(['Ordered', 'Received', 'Pending', 'Backordered']),
            'date': (datetime.now() - timedelta(days=random.randint(0, 60))).strftime('%Y-%m-%d')
        })

    # Generate operations/projects data
    projects = []
    for i in range(25):
        projects.append({
            'id': f'PRJ-{2026}-{i+1:03d}',
            'name': random.choice(['Engine Assembly Line', 'Quality Control System', 'Automation Upgrade', 'Safety Compliance', 'Process Optimization']),
            'customer': random.choice(['Aviation Corp', 'Defense Systems', 'Commercial Airlines', 'Manufacturing Giant']),
            'status': random.choice(['Active', 'Planning', 'Completed', 'On Hold']),
            'progress': random.randint(10, 95),
            'value': random.randint(50000, 500000)
        })

    # Dashboard metrics - OVER THE TOP!
    dashboard_metrics = {
        'total_revenue': 8750000,  # 8.75M EUR
        'monthly_growth': 23.7,    # 23.7% growth
        'active_projects': 47,
        'completed_orders': 234,
        'customer_satisfaction': 98.5,  # 98.5%
        'efficiency_score': 94.2,       # 94.2%
        'ai_insights_generated': 1250,
        'emails_processed': 8750,
        'leads_converted': 156,
        'cost_savings': 425000,         # 425K EUR in smart optimizations
        'on_time_delivery': 96.8,       # 96.8%
        'supplier_performance': 92.3,   # 92.3%
        'inventory_turnover': 8.5,
        'profit_margin': 34.7,          # 34.7%
        'new_customers': 89,
        'repeat_business_rate': 78.5,   # 78.5%
        'market_share_growth': 5.2,     # 5.2% increase
        'innovation_index': 87.3        # 87.3%
    }

    # Revenue chart data - last 12 months with exponential growth
    revenue_chart = {
        'labels': [(datetime.now() - timedelta(days=30*i)).strftime('%b %Y') for i in range(12)][::-1],
        'datasets': [{
            'label': 'Monthly Revenue (€)',
            'data': [650000, 720000, 680000, 780000, 850000, 920000, 980000, 1050000, 1180000, 1320000, 1480000, 1620000],
            'borderColor': 'rgba(54, 162, 235, 1)',
            'backgroundColor': 'rgba(54, 162, 235, 0.2)',
            'tension': 0.4,
            'fill': True
        }]
    }

    # Project status distribution
    project_status_chart = {
        'labels': ['Active', 'Planning', 'Completed', 'On Hold', 'Cancelled'],
        'datasets': [{
            'label': 'Projects by Status',
            'data': [23, 8, 12, 3, 1],
            'backgroundColor': [
                'rgba(54, 162, 235, 0.8)',
                'rgba(255, 205, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(255, 99, 132, 0.8)',
                'rgba(153, 102, 255, 0.8)'
            ],
            'borderWidth': 2
        }]
    }

    # Customer acquisition funnel
    funnel_chart = {
        'labels': ['Website Visitors', 'Leads Generated', 'Qualified Prospects', 'Proposals Sent', 'Deals Closed'],
        'datasets': [{
            'label': 'Conversion Funnel',
            'data': [50000, 8750, 2340, 567, 156],
            'backgroundColor': [
                'rgba(255, 99, 132, 0.8)',
                'rgba(255, 159, 64, 0.8)',
                'rgba(255, 205, 86, 0.8)',
                'rgba(75, 192, 192, 0.8)',
                'rgba(54, 162, 235, 0.8)'
            ]
        }]
    }

    # Performance metrics over time
    performance_chart = {
        'labels': [(datetime.now() - timedelta(days=7*i)).strftime('%d/%m') for i in range(12)][::-1],
        'datasets': [
            {
                'label': 'On-Time Delivery %',
                'data': [94.2, 95.1, 93.8, 96.5, 97.2, 95.8, 98.1, 94.7, 96.9, 97.5, 95.3, 96.8],
                'borderColor': 'rgba(75, 192, 192, 1)',
                'backgroundColor': 'rgba(75, 192, 192, 0.1)',
                'tension': 0.4
            },
            {
                'label': 'Customer Satisfaction %',
                'data': [97.8, 98.2, 97.5, 98.7, 99.1, 98.4, 98.9, 97.9, 98.6, 98.8, 97.7, 98.5],
                'borderColor': 'rgba(153, 102, 255, 1)',
                'backgroundColor': 'rgba(153, 102, 255, 0.1)',
                'tension': 0.4
            },
            {
                'label': 'Efficiency Score %',
                'data': [91.5, 92.8, 90.9, 93.7, 94.2, 92.6, 95.1, 91.8, 93.9, 94.7, 92.3, 94.2],
                'borderColor': 'rgba(255, 159, 64, 1)',
                'backgroundColor': 'rgba(255, 159, 64, 0.1)',
                'tension': 0.4
            }
        ]
    }

    # AI insights data
    ai_insights = [
        {
            'title': 'Cost Optimization Opportunity',
            'description': 'Identified €45,230 in potential savings by switching to alternative supplier for bearing assemblies',
            'impact': 'High',
            'confidence': 94
        },
        {
            'title': 'Lead Generation Success',
            'description': 'AI analysis of customer data revealed 23 high-potential prospects in aerospace sector',
            'impact': 'High',
            'confidence': 87
        },
        {
            'title': 'Inventory Optimization',
            'description': 'Recommended reducing safety stock for 15 part numbers, freeing €125,000 in working capital',
            'impact': 'Medium',
            'confidence': 91
        },
        {
            'title': 'Supplier Performance Alert',
            'description': 'Quality issues detected with Supplier X - recommend alternative sourcing for critical components',
            'impact': 'Critical',
            'confidence': 96
        }
    ]

    # Recent activities
    activities = []
    activity_types = ['Sale Completed', 'New Lead', 'Project Milestone', 'AI Insight', 'Order Shipped', 'Quote Sent']
    for i in range(15):
        activities.append({
            'type': random.choice(activity_types),
            'description': f'Activity {i+1} description with lots of exciting details',
            'value': random.randint(5000, 50000),
            'date': (datetime.now() - timedelta(hours=random.randint(1, 72))).strftime('%Y-%m-%d %H:%M')
        })

    # Top customers by revenue
    top_customers = [
        {'name': 'Aviation Giant Corp', 'revenue': 1250000, 'orders': 23, 'growth': 15.7},
        {'name': 'Defense Systems Ltd', 'revenue': 980000, 'orders': 18, 'growth': 22.3},
        {'name': 'Commercial Airlines Inc', 'revenue': 875000, 'orders': 31, 'growth': 8.9},
        {'name': 'Manufacturing Excellence GmbH', 'revenue': 742000, 'orders': 16, 'growth': 31.2},
        {'name': 'Precision Engineering Co', 'revenue': 689000, 'orders': 14, 'growth': 12.5}
    ]

    # Generate prospecting data
    prospects = []
    prospect_sources = ['Existing Customer Analysis', 'Industry Database', 'Email Integration', 'Web Scraping', 'Social Media']
    industries = ['Aerospace', 'Defense', 'Commercial Aviation', 'Manufacturing', 'Energy']
    for i in range(20):
        prospects.append({
            'id': f'PROS-{2026}-{i+1:03d}',
            'company': random.choice(['SkyTech Industries', 'Precision Components Ltd', 'Global Manufacturing Corp', 'Advanced Systems Inc', 'Quality Parts GmbH']),
            'industry': random.choice(industries),
            'contact': f'Contact {i+1}',
            'email': f'contact{i+1}@example.com',
            'source': random.choice(prospect_sources),
            'score': random.randint(60, 95),
            'status': random.choice(['New', 'Qualified', 'Contacted', 'Proposal', 'Closed']),
            'potential_value': random.randint(50000, 200000),
            'last_activity': (datetime.now() - timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d')
        })

    # Generate AI analysis data
    ai_parts_analysis = []
    parts = [
        'Bearing Assembly 6205', 'Hydraulic Pump P-200', 'Servo Motor SM-45', 'Gearbox Unit G-300',
        'Control Valve CV-100', 'Linear Actuator LA-75', 'Power Supply PS-500', 'Sensor Array SA-20'
    ]
    suppliers = ['Global Components', 'Industrial Parts Ltd', 'Precision Manufacturing', 'Quality Suppliers Inc']
    for i in range(12):
        part = random.choice(parts)
        current_supplier = random.choice(suppliers)
        available_suppliers = [s for s in suppliers if s != current_supplier]
        ai_parts_analysis.append({
            'part_number': f'PT-{1000+i:04d}',
            'part_name': part,
            'current_supplier': current_supplier,
            'current_price': random.randint(500, 5000),
            'recommended_supplier': random.choice(available_suppliers),
            'recommended_price': random.randint(400, 4500),
            'savings_potential': random.randint(5000, 25000),
            'confidence': random.randint(85, 98),
            'reasoning': random.choice([
                'Better quality rating with 15% lower defect rate',
                'Volume discount available for bulk orders',
                'Geographic proximity reduces shipping costs',
                'Alternative supplier offers 30-day payment terms'
            ])
        })

    # Generate price lists data
    price_lists = []
    customer_types = ['Standard', 'Premium', 'Enterprise', 'Government']
    for i in range(8):
        customer_type = random.choice(customer_types)
        base_price = random.randint(100, 2000)
        discount = {'Standard': 0, 'Premium': 5, 'Enterprise': 10, 'Government': 15}[customer_type]
        final_price = base_price * (1 - discount/100)

        price_lists.append({
            'part_number': f'PT-{2000+i:04d}',
            'description': random.choice(parts),
            'base_price': base_price,
            'customer_type': customer_type,
            'discount_percent': discount,
            'final_price': round(final_price, 2),
            'moq': random.choice([1, 10, 25, 50, 100]),
            'lead_time_days': random.randint(1, 14),
            'availability': random.choice(['In Stock', '2-3 weeks', '4-6 weeks', 'On Backorder'])
        })

    # Generate customer portal data
    portal_orders = []
    for i in range(15):
        order_date = datetime.now() - timedelta(days=random.randint(1, 60))
        portal_orders.append({
            'order_number': f'ORD-{2026}-{i+1:04d}',
            'date': order_date.strftime('%Y-%m-%d'),
            'status': random.choice(['Processing', 'Shipped', 'Delivered', 'On Hold', 'Cancelled']),
            'total_value': random.randint(5000, 50000),
            'items_count': random.randint(1, 10),
            'tracking_number': f'TR{random.randint(100000000, 999999999)}' if random.random() > 0.3 else None,
            'estimated_delivery': (order_date + timedelta(days=random.randint(3, 21))).strftime('%Y-%m-%d') if random.random() > 0.2 else None
        })

    # Portal account info
    portal_account = {
        'company_name': 'ABC Manufacturing Ltd',
        'account_number': 'ACC-2026-001',
        'credit_limit': 250000,
        'current_balance': 45670,
        'payment_terms': 'Net 30',
        'preferred_contact': 'John Smith',
        'last_login': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M')
    }

    # Generate mailbox data
    emails = []
    email_senders = [
        'john.doe@techcorp.com', 'sarah.smith@industrialsolutions.de', 'mike.johnson@manufacturinginc.com',
        'lisa.brown@globalparts.co', 'david.wilson@precisioneng.co.uk', 'anna.davis@qualitysuppliers.com',
        'robert.miller@aviationcorp.com', 'emily.garcia@defensesystems.com', 'chris.anderson@commercialairlines.com'
    ]
    email_subjects = [
        'Quote Request for Bearing Assemblies', 'Update on Order SO-2026-023', 'New Product Inquiry',
        'Delivery Schedule Confirmation', 'Payment Terms Discussion', 'Technical Specifications Review',
        'Quality Assurance Report', 'Pricing Update for Part PT-1005', 'Contract Renewal Discussion'
    ]
    for i in range(25):
        sender = random.choice(email_senders)
        subject = random.choice(email_subjects)
        received_date = datetime.now() - timedelta(hours=random.randint(1, 168))  # Last 7 days
        emails.append({
            'id': f'EML-{2026}-{i+1:03d}',
            'sender': sender,
            'sender_name': sender.split('@')[0].replace('.', ' ').title(),
            'subject': subject,
            'received': received_date.strftime('%Y-%m-%d %H:%M'),
            'read': random.random() > 0.3,
            'priority': random.choice(['Normal', 'High', 'Low']),
            'category': random.choice(['Customer Inquiry', 'Order Update', 'Supplier Communication', 'Internal']),
            'extracted_contacts': [
                {'name': sender.split('@')[0].replace('.', ' ').title(), 'email': sender, 'company': sender.split('@')[1].split('.')[0].title()}
            ] if random.random() > 0.5 else [],
            'ai_insights': random.choice([
                'Potential lead for aerospace components',
                'Follow-up required on payment terms',
                'Technical specifications need clarification',
                'Urgent quality issue reported',
                None
            ])
        })

    # Generate tickets data
    tickets = []
    ticket_categories = ['Technical Support', 'Order Issue', 'Billing Question', 'Product Information', 'Account Management']
    ticket_priorities = ['Low', 'Normal', 'High', 'Critical']
    ticket_statuses = ['Open', 'In Progress', 'Waiting for Customer', 'Resolved', 'Closed']
    for i in range(20):
        created_date = datetime.now() - timedelta(days=random.randint(1, 30))
        updated_date = created_date + timedelta(hours=random.randint(1, 72))
        tickets.append({
            'id': f'TKT-{2026}-{i+1:03d}',
            'subject': random.choice([
                'Unable to access customer portal', 'Order delay notification', 'Invoice discrepancy',
                'Product specifications request', 'Account password reset', 'Shipping tracking issue',
                'Quote approval process', 'Return authorization request', 'Technical documentation needed'
            ]),
            'customer': random.choice(['TechCorp Ltd', 'Industrial Solutions GmbH', 'Manufacturing Inc', 'Global Parts Co', 'Precision Engineering Ltd']),
            'category': random.choice(ticket_categories),
            'priority': random.choice(ticket_priorities),
            'status': random.choice(ticket_statuses),
            'created': created_date.strftime('%Y-%m-%d %H:%M'),
            'updated': updated_date.strftime('%Y-%m-%d %H:%M'),
            'assigned_to': random.choice(['John Smith', 'Sarah Johnson', 'Mike Davis', 'Lisa Wilson', 'Unassigned']),
            'description': 'Customer reported an issue with their recent order and requires immediate assistance.',
            'resolution_time_hours': random.randint(1, 48) if random.random() > 0.3 else None
        })

    return {
        'dashboard': {
            'metrics': dashboard_metrics,
            'revenue_chart': revenue_chart,
            'project_status_chart': project_status_chart,
            'funnel_chart': funnel_chart,
            'performance_chart': performance_chart,
            'ai_insights': ai_insights,
            'activities': activities,
            'top_customers': top_customers
        },
        'sales': {
            'orders': sales_orders,
            'total_value': total_sales_value,
            'active_orders': len([o for o in sales_orders if o['status'] == 'Active']),
            'completed_orders': len([o for o in sales_orders if o['status'] == 'Completed'])
        },
        'purchasing': {
            'orders': purchase_orders,
            'total_value': total_purchase_value,
            'pending_orders': len([o for o in purchase_orders if o['status'] == 'Pending']),
            'received_orders': len([o for o in purchase_orders if o['status'] == 'Received'])
        },
        'operations': {
            'projects': projects,
            'active_projects': len([p for p in projects if p['status'] == 'Active']),
            'completed_projects': len([p for p in projects if p['status'] == 'Completed']),
            'total_value': sum(p['value'] for p in projects)
        },
        'prospecting': {
            'prospects': prospects,
            'total_prospects': len(prospects),
            'qualified_leads': len([p for p in prospects if p['score'] >= 80]),
            'total_potential_value': sum(p['potential_value'] for p in prospects)
        },
        'ai_analysis': {
            'parts_analysis': ai_parts_analysis,
            'total_savings_potential': sum(p['savings_potential'] for p in ai_parts_analysis),
            'average_confidence': round(sum(p['confidence'] for p in ai_parts_analysis) / len(ai_parts_analysis), 1)
        },
        'price_lists': {
            'items': price_lists,
            'customer_types': customer_types
        },
        'portal': {
            'orders': portal_orders,
            'account': portal_account,
            'recent_orders': len([o for o in portal_orders if (datetime.now() - datetime.strptime(o['date'], '%Y-%m-%d')).days <= 30])
        },
        'mailbox': {
            'emails': emails,
            'total_emails': len(emails),
            'unread_emails': len([e for e in emails if not e['read']]),
            'high_priority': len([e for e in emails if e['priority'] == 'High']),
            'contacts_extracted': sum(len(e['extracted_contacts']) for e in emails)
        },
        'tickets': {
            'tickets': tickets,
            'total_tickets': len(tickets),
            'open_tickets': len([t for t in tickets if t['status'] in ['Open', 'In Progress', 'Waiting for Customer']]),
            'resolved_tickets': len([t for t in tickets if t['status'] in ['Resolved', 'Closed']]),
            'average_resolution_time': round(sum(t['resolution_time_hours'] for t in tickets if t['resolution_time_hours']) / len([t for t in tickets if t['resolution_time_hours']]), 1) if any(t['resolution_time_hours'] for t in tickets) else 0
        }
    }

if __name__ == '__main__':
    data = generate_demo_data()
    with open('demo_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    print("Demo data generated and saved to demo_data.json")
