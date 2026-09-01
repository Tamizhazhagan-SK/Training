-- Create BMW Cars Table
CREATE TABLE IF NOT EXISTS public.bmw_cars (
    car_id SERIAL PRIMARY KEY,
    model VARCHAR(50) NOT NULL,
    model_year INT NOT NULL,
    engine VARCHAR(50) NOT NULL,
    price DECIMAL(12, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert BMW Car Data
INSERT INTO public.bmw_cars (model, model_year, engine, price)
VALUES
    ('3 Series', 2024, '2.0L Turbocharged I4', 45500.00),
    ('5 Series', 2024, '2.0L Turbocharged I4', 57500.00),
    ('X5', 2024, '3.0L Turbocharged I6', 68000.00),
    ('M4 Competition', 2024, '3.0L Twin-Turbo I6', 82500.00),
    ('iX', 2024, 'Electric Dual Motor', 87000.00);

-- Display all records
SELECT * FROM public.bmw_cars;
