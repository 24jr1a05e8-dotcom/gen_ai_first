import streamlit as st
import requests

st.set_page_config(
    page_title="Prasanna Chowdary Currency Converter",
    page_icon="💱",
    layout="centered"
)

st.title("💱 Prasanna Chowdary Currency Converter")
st.write("Convert currencies easily using live exchange rates.")

st.divider()

currencies = {
    "US Dollar": "USD",
    "Indian Rupee": "INR",
    "Euro": "EUR",
    "British Pound": "GBP",
    "Japanese Yen": "JPY",
    "Australian Dollar": "AUD",
    "Canadian Dollar": "CAD",
    "Singapore Dollar": "SGD",
    "Swiss Franc": "CHF",
    "Chinese Yuan": "CNY"
}

col1, col2 = st.columns(2)

with col1:
    amount = st.number_input(
        "💰 Enter Amount",
        min_value=0.01,
        value=1.0,
        step=0.01
    )

with col2:
    from_currency = st.selectbox(
        "From Currency",
        list(currencies.keys())
    )

to_currency = st.selectbox(
    "To Currency",
    list(currencies.keys())
)

st.divider()

if st.button("💱 Convert Currency", use_container_width=True):

    from_code = currencies[from_currency]
    to_code = currencies[to_currency]

    if from_code == to_code:
        result = amount

        st.success(
            f"{amount:.2f} {from_code} = {result:.2f} {to_code}"
        )

    else:
        try:
            url = (
                f"https://api.frankfurter.app/latest"
                f"?amount={amount}"
                f"&from={from_code}"
                f"&to={to_code}"
            )

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()

            result = data["rates"][to_code]

            exchange_rate = result / amount

            st.success(
                f"💰 {amount:.2f} {from_code} = "
                f"{result:.2f} {to_code}"
            )

            st.info(
                f"📊 Exchange Rate: "
                f"1 {from_code} = {exchange_rate:.4f} {to_code}"
            )

        except requests.RequestException:
            st.error(
                "❌ Unable to fetch exchange rates. "
                "Please check your internet connection."
            )

        except KeyError:
            st.error(
                "❌ Exchange rate is currently unavailable."
            )

st.divider()

st.caption(
    "Built with Python and Streamlit by Prasanna Chowdary"
)