from pathlib import Path

path = Path("index.html")
text = path.read_text(encoding="utf-8")

hero_start = text.index("  <!-- HERO -->")
vision_start = text.index("  <!-- VISION -->")
contact_start = text.index("  <!-- CONTACT -->")
footer_start = text.index("  <!-- FOOTER -->")

new_main = r'''  <!-- HERO -->
  <section class="hero" id="hero">
    <div class="hero-bg"></div>
    <div class="hero-overlay"></div>
    <div class="hero-content welcome-content">
      <span class="hero-eyebrow">Welcome to Vagmi Exim</span>
      <h1 class="hero-title">Global Trade.<br><em>Indian Roots.</em></h1>
      <p class="hero-sub">We connect buyers with dependable product sources from India's traditional, agricultural, cultural, and industrial strength.</p>
      <div class="welcome-products" aria-label="Product highlights">
        <a href="#products" class="welcome-product" data-category-link="powders">
          <span>Dehydrated Powders</span>
          <small>Vegetable, fruit, and spice powders</small>
        </a>
        <a href="#products" class="welcome-product" data-category-link="agri">
          <span>Agricultural Goods</span>
          <small>Grains, pulses, spices, and oil seeds</small>
        </a>
        <a href="#products" class="welcome-product" data-category-link="minerals">
          <span>Coal &amp; Minerals</span>
          <small>Bulk minerals and trade materials</small>
        </a>
        <a href="#products" class="welcome-product" data-category-link="feed">
          <span>Animal Feed</span>
          <small>DOC and feed ingredients</small>
        </a>
      </div>
      <div class="hero-actions">
        <a href="#products" class="btn-primary">Explore Products</a>
        <a href="#about" class="btn-ghost">About Us</a>
      </div>
    </div>
    <div class="hero-scroll">↓</div>
  </section>

  <!-- ABOUT -->
  <section class="section about-section" id="about">
    <div class="container about-grid">
      <div class="about-text reveal">
        <span class="label">About Us</span>
        <h2>Merchant Experts for Traditional Indian Products</h2>
        <p>Firstly, we are merchant experts. We find the right source of the product for you from the traditional and cultural roots of India, matching your taste and preferences with the highest and truly exceptional quality standards.</p>
        <p>India is rich in cultural heritage, and we work in traditional products to give our customers a better taste of satisfaction. We focus on authenticity, reliable sourcing, careful quality checks, and long-term trust.</p>
        <a href="#contact" class="btn-primary">Send Inquiry on WhatsApp</a>
      </div>
      <div class="about-stats reveal delay-1">
        <div class="stat-card">
          <span class="stat-num">Expert</span>
          <span class="stat-label">Merchant Sourcing</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">India</span>
          <span class="stat-label">Traditional Roots</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">Tailored</span>
          <span class="stat-label">Taste &amp; Preference</span>
        </div>
        <div class="stat-card">
          <span class="stat-num">High</span>
          <span class="stat-label">Quality Standards</span>
        </div>
      </div>
    </div>
  </section>

  <!-- PRODUCTS -->
  <section class="section products-section" id="products">
    <div class="container">
      <div class="section-header reveal">
        <span class="label">Product Categories</span>
        <h2>Choose a Category to View Products</h2>
        <p class="section-sub">Click a category to see sample products. Use "See All" to expand the full list, or request a specific product through WhatsApp.</p>
      </div>

      <div class="category-tabs reveal" aria-label="Product categories">
        <button class="category-tab active" type="button" data-category="powders">Dehydrated Powders</button>
        <button class="category-tab" type="button" data-category="agri">Agricultural Goods</button>
        <button class="category-tab" type="button" data-category="minerals">Coal &amp; Minerals</button>
        <button class="category-tab" type="button" data-category="feed">Animal Feed</button>
      </div>

      <div class="category-panels">
        <div class="product-panel active" data-panel="powders">
          <div class="product-panel-head">
            <div>
              <span class="label">Dehydrated Powders</span>
              <h3>Vegetable, Fruit &amp; Spice Powders</h3>
            </div>
            <button class="btn-primary see-all-btn" type="button">See All</button>
          </div>
          <div class="product-gallery">
            <article class="gallery-card">
              <img src="images/CARROT_POWDER.webp" alt="Carrot Powder" loading="lazy">
              <h4>Carrot Powder</h4>
            </article>
            <article class="gallery-card">
              <img src="images/TOMATO_POWDER.jpg" alt="Tomato Powder" loading="lazy">
              <h4>Tomato Powder</h4>
            </article>
            <article class="gallery-card">
              <img src="images/GARLIC_POWDER.jpg" alt="Garlic Powder" loading="lazy">
              <h4>Garlic Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/GINGER_POWDER.jpg" alt="Ginger Powder" loading="lazy">
              <h4>Ginger Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/RED_ONION_POWDER.jpg" alt="Red Onion Powder" loading="lazy">
              <h4>Red Onion Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/Potato-Powder.jpg" alt="Potato Powder" loading="lazy">
              <h4>Potato Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/dehydrated-mint-powder.jpg" alt="Mint Powder" loading="lazy">
              <h4>Mint Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/LEMON_POWDER.jpg" alt="Lemon Powder" loading="lazy">
              <h4>Lemon Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/orange-extract-powder.jpg" alt="Orange Extract Powder" loading="lazy">
              <h4>Orange Extract Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/high-quality-pomegranate-powder.jpg" alt="Pomegranate Powder" loading="lazy">
              <h4>Pomegranate Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/PAPAYA_POWDER.jpg" alt="Papaya Powder" loading="lazy">
              <h4>Papaya Powder</h4>
            </article>
            <article class="gallery-card extra-product">
              <img src="images/spray-dried-banana-powder-500x500.webp" alt="Banana Powder" loading="lazy">
              <h4>Banana Powder</h4>
            </article>
          </div>
          <a href="#contact" class="btn-ghost product-request" data-product-request="Dehydrated Powders">Request a Product</a>
        </div>

        <div class="product-panel" data-panel="agri">
          <div class="product-panel-head">
            <div>
              <span class="label">Agricultural Goods</span>
              <h3>Grains, Pulses, Spices &amp; Oil Seeds</h3>
            </div>
            <button class="btn-primary see-all-btn" type="button">See All</button>
          </div>
          <div class="simple-products">
            <span>Wheat</span><span>Rice</span><span>Maize</span>
            <span class="extra-product">Split Pulses</span><span class="extra-product">Kabuli Chana</span><span class="extra-product">Basmati Rice</span>
            <span class="extra-product">Indian Spices</span><span class="extra-product">Soybean</span><span class="extra-product">Oil Seeds</span>
          </div>
          <a href="#contact" class="btn-ghost product-request" data-product-request="Agricultural Goods">Request a Product</a>
        </div>

        <div class="product-panel" data-panel="minerals">
          <div class="product-panel-head">
            <div>
              <span class="label">Coal &amp; Minerals</span>
              <h3>Bulk Trade Materials</h3>
            </div>
            <button class="btn-primary see-all-btn" type="button">See All</button>
          </div>
          <div class="simple-products">
            <span>Coal 4000-6200 GAR</span><span>South African Coal RB1</span><span>South African Coal RB2</span>
            <span class="extra-product">South African Coal RB3</span><span class="extra-product">Iron Ore</span><span class="extra-product">Manganese Ore</span>
            <span class="extra-product">Calcium Carbide</span><span class="extra-product">Custom Mineral Inquiry</span>
          </div>
          <a href="#contact" class="btn-ghost product-request" data-product-request="Coal and Minerals">Request a Product</a>
        </div>

        <div class="product-panel" data-panel="feed">
          <div class="product-panel-head">
            <div>
              <span class="label">Animal Feed</span>
              <h3>Feed Ingredients &amp; Blends</h3>
            </div>
            <button class="btn-primary see-all-btn" type="button">See All</button>
          </div>
          <div class="simple-products">
            <span>Soya De-Oiled Cake (DOC)</span><span>Animal Feed Blends</span><span>Feed Ingredients</span>
            <span class="extra-product">Custom Feed Requirement</span><span class="extra-product">Bulk Supply Inquiry</span>
          </div>
          <a href="#contact" class="btn-ghost product-request" data-product-request="Animal Feed">Request a Product</a>
        </div>
      </div>
    </div>
  </section>

  <!-- PROCESS FLOWCHART -->
  <section class="section process-section" id="process">
    <div class="container">
      <div class="section-header reveal">
        <span class="label">How We Work</span>
        <h2>Document Flow</h2>
        <p class="section-sub">A clear flow from product enquiry to final payment, covering specifications, contract terms, shipment and documentation.</p>
      </div>
      <div class="flow-grid flow-grid-five">
        <div class="flow-phase reveal">
          <div class="phase-num">01</div>
          <div class="phase-label">Pre-Shipment</div>
          <ul>
            <li>Product enquiry and requirement discussion</li>
            <li>Sampling, if required</li>
            <li>Price negotiation with Incoterms such as FOB or CIF</li>
            <li>Specification and Certificate of Analysis review</li>
            <li>Price and conditions agreed</li>
          </ul>
        </div>
        <div class="flow-arrow reveal">→</div>
        <div class="flow-phase reveal delay-1">
          <div class="phase-num">02</div>
          <div class="phase-label">Contract</div>
          <ul>
            <li>Contract signed by both parties</li>
            <li>LC, SBLC or BG applied as per terms</li>
            <li>Payment received as per contract</li>
          </ul>
        </div>
        <div class="flow-arrow reveal">→</div>
        <div class="flow-phase reveal delay-2">
          <div class="phase-num">03</div>
          <div class="phase-label">Preparation</div>
          <ul>
            <li>Goods manufactured or sourced</li>
            <li>Quality tested before dispatch</li>
            <li>Packed according to international maritime or air standards</li>
            <li>Other technical requirements completed as mentioned in the contract</li>
          </ul>
        </div>
        <div class="flow-arrow reveal">→</div>
        <div class="flow-phase reveal delay-3">
          <div class="phase-num">04</div>
          <div class="phase-label">Delivery</div>
          <ul>
            <li>Loading and transshipment coordination</li>
            <li>Inspection completed</li>
            <li>Payment released to supplier</li>
          </ul>
        </div>
        <div class="flow-arrow reveal">→</div>
        <div class="flow-phase reveal delay-3">
          <div class="phase-num">05</div>
          <div class="phase-label">Payment</div>
          <ul>
            <li>Submission of all documents from proforma invoice to bill of lading</li>
            <li>LC or TT processed for final payment</li>
          </ul>
        </div>
      </div>
    </div>
  </section>

'''

new_contact = r'''  <!-- CONTACT -->
  <section class="section contact-section" id="contact">
    <div class="container contact-grid">
      <div class="contact-info reveal">
        <span class="label white-label">Contact Us</span>
        <h2 class="white-h">Send Your Inquiry</h2>
        <p class="white-p">Share your product requirement and we will continue the inquiry directly on WhatsApp.</p>
        <div class="contact-details">
          <div class="contact-item">
            <span class="c-icon">📍</span>
            <div>
              <strong>Address</strong><br>
              R6/294, Naik Niwas, Ganj Golai East,<br>Latur - 413512, Maharashtra, India
            </div>
          </div>
          <div class="contact-item">
            <span class="c-icon">📧</span>
            <div>
              <strong>Email</strong><br>
              <a href="mailto:info@vagmiexim.com">info@vagmiexim.com</a><br>
              <a href="mailto:sales@vagmiexim.com">sales@vagmiexim.com</a><br>
              <a href="mailto:purchase@vagmiexim.com">purchase@vagmiexim.com</a>
            </div>
          </div>
          <div class="contact-item">
            <span class="c-icon">📞</span>
            <div>
              <strong>Mobile</strong><br>
              <a href="tel:+917499770195">+91 74997 70195</a>
            </div>
          </div>
          <div class="contact-item">
            <span class="c-icon">💬</span>
            <div>
              <strong>WhatsApp</strong><br>
              <a href="#contact" class="whatsapp-inquiry-link">Send inquiry through WhatsApp</a>
            </div>
          </div>
        </div>
      </div>
      <div class="contact-form reveal delay-1">
        <form class="contact-form" onsubmit="handleForm(event)">
          <div class="form-group">
            <label>Name</label>
            <input type="text" id="name" required>
          </div>

          <div class="form-group">
            <label>Email</label>
            <input type="email" id="email" required>
          </div>

          <div class="form-group">
            <label>Phone</label>
            <input type="tel" id="phone" required>
          </div>

          <div class="form-group">
            <label>Product Category</label>
            <select id="productCategory" required>
              <option value="">Select category</option>
              <option>Dehydrated Powders</option>
              <option>Agricultural Goods</option>
              <option>Coal and Minerals</option>
              <option>Animal Feed</option>
              <option>Other Product</option>
            </select>
          </div>

          <div class="form-group">
            <label>Message</label>
            <textarea id="message" rows="5" required placeholder="Tell us product name, quantity, destination, and sampling requirement."></textarea>
          </div>

          <button type="submit" class="btn-primary full-width">
            Send Message Inquiry to WhatsApp
          </button>

          <div id="formMsg" class="form-msg"></div>
        </form>
      </div>
    </div>
  </section>

'''

text = text[:hero_start] + new_main + new_contact + text[footer_start:]

nav_start = text.index("      <ul class=\"nav-links\">")
nav_end = text.index("      </ul>", nav_start) + len("      </ul>")
new_nav = r'''      <ul class="nav-links">
        <li><a href="#hero">Home</a></li>
        <li><a href="#about">About</a></li>
        <li><a href="#products">Products</a></li>
        <li><a href="#process">How We Work</a></li>
        <li><a href="#contact" class="nav-cta">Contact Us</a></li>
      </ul>'''
text = text[:nav_start] + new_nav + text[nav_end:]

mobile_start = text.index("    <div class=\"mobile-menu\"")
mobile_end = text.index("    </div>", mobile_start) + len("    </div>")
new_mobile = r'''    <div class="mobile-menu" id="mobileMenu">
      <a href="#hero" onclick="closeMobile()">Home</a>
      <a href="#about" onclick="closeMobile()">About</a>
      <a href="#products" onclick="closeMobile()">Products</a>
      <a href="#process" onclick="closeMobile()">How We Work</a>
      <a href="#contact" onclick="closeMobile()">Contact Us</a>
    </div>'''
text = text[:mobile_start] + new_mobile + text[mobile_end:]

text = text.replace('<a href="#powders">Powders</a>', '<a href="#products">Products</a>')
text = text.replace('<a href="#process">Process</a>', '<a href="#process">How We Work</a>')
text = text.replace('Import Â· Export Â· Trading', 'Import · Export · Trading')
text = text.replace('Â© 2025 Vagmi Exim. All rights reserved. Â· Latur, Maharashtra, India', '© 2025 Vagmi Exim. All rights reserved. · Latur, Maharashtra, India')
text = text.replace('href="https://wa.me/919422014528"', 'href="#contact"')

path.write_text(text, encoding="utf-8", newline="\r\n")
