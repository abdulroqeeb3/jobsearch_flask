from flask import Flask, render_template_string

app = Flask(__name__)

html_content = """
<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Job Search Services | Get Hired Faster</title>
  <link href=\"https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css\" rel=\"stylesheet\">
</head>
<body class=\"bg-gray-50 text-gray-800\">
  <header class=\"bg-white shadow p-6\">
    <div class=\"max-w-7xl mx-auto text-center\">
      <h1 class=\"text-3xl font-bold\">Land Your Dream Job Faster</h1>
      <p class=\"text-lg mt-2\">Professional Resumes, LinkedIn Optimization & Job Strategy That Get You Hired</p>
    </div>
  </header>

  <section class=\"py-12 px-6 max-w-4xl mx-auto\">
    <h2 class=\"text-2xl font-semibold mb-4\">Tired of Being Ignored by Recruiters?</h2>
    <p class=\"mb-6\">You're not the problem — your resume, LinkedIn profile, and job search approach are. Let me help you <strong>stand out</strong>, get noticed, and land high-paying roles — even in competitive markets.</p>

    <h3 class=\"text-xl font-semibold mb-2\">Who This Is For:</h3>
    <ul class=\"list-disc list-inside mb-6\">
      <li>Mid-level & senior professionals stuck in stagnant jobs</li>
      <li>International job seekers (UK, US, Canada, etc.)</li>
      <li>Remote workers looking to upgrade their income</li>
      <li>Tech, finance, healthcare, marketing, and admin pros</li>
    </ul>

    <h3 class=\"text-xl font-semibold mb-4\">Choose Your Package:</h3>
    <div class=\"grid grid-cols-1 md:grid-cols-3 gap-6\">
      <div class=\"bg-white p-6 rounded-lg shadow\">
        <h4 class=\"text-lg font-bold mb-2\">Basic – $150</h4>
        <ul class=\"list-disc list-inside text-sm mb-4\">
          <li>Rewritten resume (ATS-optimized)</li>
          <li>PDF + Word format</li>
          <li>3–5 business day turnaround</li>
        </ul>
        <button class=\"bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700\">Book Now</button>
      </div>
      <div class=\"bg-white p-6 rounded-lg shadow border-2 border-blue-500\">
        <h4 class=\"text-lg font-bold mb-2\">Pro – $300</h4>
        <ul class=\"list-disc list-inside text-sm mb-4\">
          <li>Resume</li>
          <li>LinkedIn Optimization</li>
          <li>Custom Cover Letter</li>
          <li>2 revision rounds</li>
        </ul>
        <button class=\"bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700\">Book Now</button>
      </div>
      <div class=\"bg-white p-6 rounded-lg shadow\">
        <h4 class=\"text-lg font-bold mb-2\">Premium VIP – $500</h4>
        <ul class=\"list-disc list-inside text-sm mb-4\">
          <li>All in Pro Package</li>
          <li>1-on-1 Zoom Strategy Call</li>
          <li>Job Search Action Plan</li>
          <li>Mock Interview Prep</li>
          <li>Priority 2–3 day delivery</li>
        </ul>
        <button class=\"bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700\">Book Now</button>
      </div>
    </div>
  </section>

  <section class=\"bg-gray-100 py-12 px-6\">
    <div class=\"max-w-4xl mx-auto text-center\">
      <h3 class=\"text-xl font-semibold mb-4\">Why Clients Trust Me:</h3>
      <ul class=\"list-disc list-inside text-left inline-block text-sm\">
        <li>100+ resumes rewritten</li>
        <li>85% client success rate (interview in 30 days)</li>
        <li>Clients hired at Amazon, NHS, Shopify, Meta & more</li>
      </ul>
    </div>
  </section>

  <section class=\"text-center py-8\">
    <a href=\"https://calendly.com/yourusername\" target=\"_blank\">
      <button class=\"bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700\">Book a Free Consultation</button>
    </a>
    <p class=\"mt-4\">Or message me directly on WhatsApp:</p>
    <a href=\"https://wa.me/16812964100\" target=\"_blank\">
      <button class=\"bg-green-600 text-white px-6 py-2 mt-2 rounded hover:bg-green-700\">Chat on WhatsApp</button>
    </a>
  </section>

  <footer class=\"bg-white py-6 mt-12 text-center\">
    <p class=\"text-sm\">Ready to get hired faster? Book your package now and let's make it happen.</p>
    <a href=\"https://calendly.com/yourusername\" target=\"_blank\">
      <button class=\"mt-4 bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700\">Book My Resume Service</button>
    </a>
  </footer>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)
