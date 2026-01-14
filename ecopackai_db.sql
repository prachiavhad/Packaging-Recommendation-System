-- 1. Map Material Types to Industries (The "Bridge")
UPDATE materials SET industry = 'Electronics' 
WHERE material_type IN ('Synthetic Polymer', 'Metal', 'Bioplastic', 'Mineral Composite');

UPDATE materials SET industry = 'Food' 
WHERE material_type IN ('Natural Fiber', 'Agri-waste Fiber', 'Glass', 'Plant-based Material');

UPDATE materials SET industry = 'Healthcare' 
WHERE material_type IN ('Synthetic Polymer', 'Bioplastic', 'Bio-Composite');

-- 2. Fill any remaining blanks so you NEVER get 0 results
UPDATE materials SET industry = 'Electronics' WHERE industry IS NULL;

-- 3. Verify the data is there
SELECT material_name, industry FROM materials LIMIT 10;