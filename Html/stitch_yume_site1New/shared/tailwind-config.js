window.tailwind = window.tailwind || {};
window.tailwind.config = {
    darkMode: "class",
    theme: {
        extend: {
            colors: {
                "primary": "#0369A1",
                "primary-light": "#0284C7",
                "primary-dark": "#2B4D66",
                "secondary": "#E6F0F7",
                "line": "#DCEAF4",
                "line-strong": "#0284C7",
                "accent": "#2B4D66",
                "background-light": "#FFFFFF",
                "background-subtle": "#F8FAFC",
                "background-dark": "#0B1120",
                "surface-light": "#FFFFFF",
                "surface-dark": "#1E293B",
                "text-main": "#334155",
                "text-light": "#64748B",
                "text-heading": "#0F172A",
                "line-green": "#06C755",
            },
            fontFamily: {
                "display": ["Plus Jakarta Sans", "Noto Sans JP", "sans-serif"],
                "body": ["Noto Sans JP", "sans-serif"],
            },
            boxShadow: {
                "soft": "0 4px 6px -1px rgba(0, 0, 0, 0.02), 0 2px 4px -1px rgba(0, 0, 0, 0.02)",
                "card": "0 10px 15px -3px rgba(0, 0, 0, 0.03), 0 4px 6px -2px rgba(0, 0, 0, 0.01)",
                "floating": "0 20px 25px -5px rgba(0, 0, 0, 0.05), 0 10px 10px -5px rgba(0, 0, 0, 0.01)",
                "glow": "0 0 20px rgba(2, 132, 199, 0.3)",
                "xl": "0 20px 30px rgba(0, 0, 0, 0.08)",
                "2xl": "0 28px 44px rgba(0, 0, 0, 0.1)",
            },
            backgroundImage: {
                "gradient-primary": "linear-gradient(135deg, #0369A1 0%, #2B4D66 100%)",
                "gradient-surface": "linear-gradient(to bottom right, #ffffff, #f8fafc)",
            },
            animation: {
                "fade-in-up": "fadeInUp 0.8s ease-out forwards",
                "float": "float 6s ease-in-out infinite",
            },
            keyframes: {
                fadeInUp: {
                    "0%": { opacity: "0", transform: "translateY(20px)" },
                    "100%": { opacity: "1", transform: "translateY(0)" },
                },
                float: {
                    "0%, 100%": { transform: "translateY(0)" },
                    "50%": { transform: "translateY(-10px)" },
                },
            },
            borderRadius: {
                "DEFAULT": "0.25rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "full": "9999px",
            },
        },
    },
};
