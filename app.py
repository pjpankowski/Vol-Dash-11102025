"""
FIXED: Professional Volatility Platform - Sidebar Navigation
All features accessible - No hidden tabs issue
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Volatility Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# LIGHT THEME
# ==========================================

st.markdown("""
<style>
    .stApp { background-color: #FFFFFF; }
    h1, h2, h3 { color: #1E3A8A; font-weight: 600; }
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #1E3A8A;
        font-weight: 600;
    }
    [data-testid="stMetricLabel"] {
        color: #64748B;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA LOADING
# ==========================================

@st.cache_data
def load_all_data():
    data = {}
    files = [
        'vix_term_structure', 'volatility_surface', 'barra_factors', 'variance_premium',
        'factor_attribution', 'vol_regime', 'trade_signals', 'portfolio_greeks',
        'etf_arbitrage_microstructure', 'grinold_kahn_strategies', 'alpha_factors_ml',
        'order_flow_toxicity', 'etf_basket_composition', 'risk_budgeting_optimization',
        'ml_feature_importance', 'global_equity_dislocations', 'variance_swap_pricing',
        'dividend_futures_arbitrage', 'vix_term_structure_forecast', 'option_greeks_dynamic_hedging',
        'volatility_forecasting_models', 'live_market_snapshot', 'trade_execution_journal',
        'alert_rules', 'alert_history', 'scenario_analysis', 'research_daily_notes',
        'performance_attribution_daily', 'economic_calendar', 'correlation_network'
    ]
    
    for file in files:
        try:
            data[file] = pd.read_csv(f'{file}.csv')
        except:
            data[file] = pd.DataFrame()
    
    return data

data = load_all_data()

# ==========================================
# SIDEBAR NAVIGATION (SOLUTION TO TAB LIMIT)
# ==========================================

st.sidebar.title("📊 Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Analysis Module:",
    [
        "🎯 Command Center",
        "📊 Live Market",
        "💼 Trade Journal",
        "🚨 Alert Center",
        "📉 Stress Tests",
        "📝 Research Notes",
        "📊 Performance",
        "🌍 Global Markets",
        "📈 VIX Ecosystem",
        "🔷 3D Vol Surface",
        "💎 Variance Swaps",
        "💰 Dividends",
        "🔮 Forecasting",
        "📐 Factor Analysis",
        "⚖️ Optimization",
        "🏪 ETF Flow",
        "🌊 Order Flow",
        "🤖 ML Alpha",
        "🎲 Greeks",
        "📅 Economic Calendar",
        "🎨 3D Analytics"
    ]
)

# ==========================================
# HEADER
# ==========================================

st.title("📊 Professional Volatility Analytics Platform")
st.markdown("**Institutional-Grade Market Intelligence with Advanced 3D Visualizations**")
st.markdown("---")

# Status bar
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("🟢 **Market:** OPEN")
with col2:
    st.markdown("📊 **VIX:** 18.45")
with col3:
    st.markdown("⏰ **FOMC:** 12 days")
with col4:
    st.markdown(f"📅 **{datetime.now().strftime('%I:%M %p')}**")

st.markdown("---")

# ==========================================
# PAGE ROUTING
# ==========================================

if page == "🎯 Command Center":
    st.header("🎯 Executive Command Center")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric("VIX Spot", "18.45", "+1.2")
    with col2:
        st.metric("S&P 500", "5,847", "+12.5")
    with col3:
        st.metric("VRP", "3.45", "+0.3")
    with col4:
        st.metric("SPY Premium", "2.6 bps")
    with col5:
        st.metric("Portfolio P&L", "$6.2M", "+2.3%")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Top Strategies by IR")
        if not data['grinold_kahn_strategies'].empty:
            gk = data['grinold_kahn_strategies'].sort_values('Expected_IR', ascending=False)
            st.dataframe(gk[['Strategy', 'Expected_IR', 'Expected_Alpha']], 
                        use_container_width=True, hide_index=True)
    
    with col2:
        st.subheader("🎯 Portfolio Greeks")
        if not data['portfolio_greeks'].empty:
            greeks = data['portfolio_greeks']
            st.metric("Total Vega", f"{greeks['Vega'].sum():,.0f}")
            st.metric("Total Gamma", f"{greeks['Gamma'].sum():,.2f}")
            st.metric("Total Delta", f"{greeks['Delta'].sum():,.0f}")

elif page == "📊 Live Market":
    st.header("📊 Live Market Dashboard")
    
    if not data['live_market_snapshot'].empty:
        live = data['live_market_snapshot'].iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("VIX Spot", f"{live['VIX_Spot']:.2f}")
        with col2:
            st.metric("SPX", f"${live['SPX_Price']:.2f}")
        with col3:
            st.metric("VRP", f"{live['VRP_Current']:.2f}")
        with col4:
            st.metric("Market", f"🟢 {live['Market_Status']}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("VIX Futures Curve")
            curve_data = pd.DataFrame({
                'Tenor': ['Spot', '1M', '2M', '3M'],
                'Level': [live['VIX_Spot'], live['VIX_1M_Future'], 
                         live['VIX_2M_Future'], live['VIX_3M_Future']]
            })
            fig = px.line(curve_data, x='Tenor', y='Level', markers=True)
            fig.update_traces(line_color='#1E3A8A')
            fig.update_layout(height=400, plot_bgcolor='white')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("ETF Flow")
            st.metric("SPY Price", f"${live['SPY_Price']:.2f}")
            st.metric("Premium", f"{live['SPY_Premium_bps']:.2f} bps")
            st.metric("Creations", live['SPY_Creation_Units_Today'])
            st.metric("Redemptions", live['SPY_Redemption_Units_Today'])

elif page == "💼 Trade Journal":
    st.header("💼 Trade Execution & Journal")
    
    if not data['trade_execution_journal'].empty:
        trades = data['trade_execution_journal']
        
        col1, col2, col3, col4 = st.columns(4)
        closed = trades[trades['Status'] == 'Closed']
        
        with col1:
            st.metric("Total Trades", len(trades))
        with col2:
            st.metric("Open", len(trades[trades['Status'] == 'Open']))
        with col3:
            if not closed.empty:
                st.metric("Total P&L", f"${closed['PnL_USD'].sum():,.0f}")
        with col4:
            if not closed.empty and len(closed) > 0:
                win_rate = (closed['PnL_USD'] > 0).sum() / len(closed)
                st.metric("Win Rate", f"{win_rate:.1%}")
        
        st.markdown("---")
        st.dataframe(trades[['Entry_Date', 'Strategy', 'Direction', 'Status']].head(20),
                    use_container_width=True, hide_index=True)

elif page == "🚨 Alert Center":
    st.header("🚨 Alert Center")
    
    if not data['alert_rules'].empty:
        st.subheader("Alert Rules")
        st.dataframe(data['alert_rules'][['Alert_Name', 'Condition', 'Priority']],
                    use_container_width=True, hide_index=True)
    
    if not data['alert_history'].empty:
        st.markdown("---")
        st.subheader("Recent Alerts")
        st.dataframe(data['alert_history'][['Timestamp', 'Alert_Name', 'Priority']].head(15),
                    use_container_width=True, hide_index=True)

elif page == "📉 Stress Tests":
    st.header("📉 Scenario Analysis")
    
    if not data['scenario_analysis'].empty:
        scenarios = data['scenario_analysis']
        
        selected = st.selectbox("Select Scenario:", scenarios['Scenario_Name'].tolist())
        scenario = scenarios[scenarios['Scenario_Name'] == selected].iloc[0]
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("SPX Move", f"{scenario['SPX_Move_Pct']:.1f}%")
        with col2:
            st.metric("VIX", f"{scenario['VIX_Level']:.1f}")
        with col3:
            st.metric("Total P&L", f"${scenario['Total_Portfolio_PnL']:,.0f}")
        with col4:
            st.metric("Max DD", f"{scenario['Max_Drawdown_Pct']:.1f}%")
        
        st.markdown("---")
        
        pnl_data = pd.DataFrame({
            'Strategy': ['Variance Swaps', 'VIX Calls', 'ETF Arb'],
            'P&L': [scenario['Variance_Swap_PnL'], 
                   scenario['VIX_Call_Spread_PnL'],
                   scenario['ETF_NAV_Arb_PnL']]
        })
        fig = px.bar(pnl_data, x='Strategy', y='P&L', color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)

elif page == "📝 Research Notes":
    st.header("📝 Research Commentary")
    
    if not data['research_daily_notes'].empty:
        notes = data['research_daily_notes']
        latest = notes.iloc[0]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("VIX", f"{latest['VIX_Close']:.2f}", f"{latest['VIX_Change']:+.2f}")
        with col2:
            st.metric("SPX", f"{latest['SPX_Close']:.2f}")
        with col3:
            st.metric("VRP", f"{latest['VRP']:.2f}")
        
        st.markdown("---")
        st.markdown(f"**Summary:** {latest['Market_Summary']}")
        st.markdown(f"**Observation:** {latest['Key_Observation']}")
        st.markdown(f"**Trade Idea:** {latest['Trade_Idea']}")

elif page == "📊 Performance":
    st.header("📊 Performance Attribution")
    
    if not data['performance_attribution_daily'].empty:
        perf = data['performance_attribution_daily']
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=perf.index, y=perf['Cumulative_PnL'],
                                fill='tozeroy', line=dict(color='#1E3A8A')))
        fig.update_layout(height=400, plot_bgcolor='white', title="Cumulative P&L")
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total P&L", f"${perf['Cumulative_PnL'].iloc[-1]:,.0f}")
        with col2:
            st.metric("Avg Sharpe", f"{perf['Sharpe_30D'].mean():.2f}")
        with col3:
            st.metric("Win Rate", f"{perf['Win_Rate_30D'].mean():.1%}")

elif page == "🌍 Global Markets":
    st.header("🌍 Global Markets")
    
    if not data['global_equity_dislocations'].empty:
        global_data = data['global_equity_dislocations'].tail(100)
        
        # 3D scatter plot
        fig = go.Figure(data=[go.Scatter3d(
            x=global_data['US_RV'],
            y=global_data['Europe_RV'],
            z=global_data['Asia_RV'],
            mode='markers',
            marker=dict(
                size=5,
                color=global_data['Dislocation_Score'],
                colorscale='RdYlGn_r',
                showscale=True
            )
        )])
        
        fig.update_layout(
            title="3D Volatility Correlation",
            scene=dict(
                xaxis_title='US Vol',
                yaxis_title='Europe Vol',
                zaxis_title='Asia Vol'
            ),
            height=700
        )
        st.plotly_chart(fig, use_container_width=True)
        
        arb_opps = global_data[global_data['Arbitrage_Opportunity'] == 'Yes']
        st.metric("Arbitrage Opportunities", len(arb_opps))

elif page == "📈 VIX Ecosystem":
    st.header("📈 VIX Ecosystem")
    
    if not data['vix_term_structure'].empty:
        vix = data['vix_term_structure']
        fig = px.line(vix, x='Tenor', y='Implied_Vol', markers=True)
        fig.update_traces(line_color='#1E3A8A')
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(vix, use_container_width=True, hide_index=True)

elif page == "🔷 3D Vol Surface":
    st.header("🔷 3D Volatility Surface")
    
    if not data['volatility_surface'].empty:
        vol_surf = data['volatility_surface']
        
        # Create 3D surface
        pivot = vol_surf.pivot(index='Strike', columns='Maturity_Days', values='Implied_Vol')
        
        fig = go.Figure(data=[go.Surface(
            z=pivot.values,
            x=pivot.columns,
            y=pivot.index,
            colorscale='Blues'
        )])
        
        fig.update_layout(
            title="3D Volatility Surface",
            scene=dict(
                xaxis_title='Maturity (Days)',
                yaxis_title='Strike',
                zaxis_title='Implied Vol'
            ),
            height=700
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.info("💡 Drag to rotate, scroll to zoom")

# Continue with remaining pages...
# (Adding more elif statements for each page)

elif page == "💎 Variance Swaps":
    st.header("💎 Variance Swaps")
    
    if not data['variance_swap_pricing'].empty:
        var_swap = data['variance_swap_pricing']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg Payoff", f"${var_swap['Payoff_USD'].mean():,.0f}")
        with col2:
            st.metric("Avg Vega", f"${var_swap['Vega_Notional'].mean():,.0f}")
        with col3:
            st.metric("Convexity", f"${var_swap['Convexity_Value'].mean():,.2f}")
        
        st.dataframe(var_swap[['Date', 'Var_Strike', 'Realized_Var', 'Payoff_USD']].head(20),
                    use_container_width=True, hide_index=True)

elif page == "💰 Dividends":
    st.header("💰 Dividend Futures")
    
    if not data['dividend_futures_arbitrage'].empty:
        div_fut = data['dividend_futures_arbitrage']
        fig = px.bar(div_fut, x='Quarter', y='Arb_PnL_Per_1000',
                    color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(div_fut, use_container_width=True, hide_index=True)

elif page == "🔮 Forecasting":
    st.header("🔮 Volatility Forecasting")
    
    if not data['volatility_forecasting_models'].empty:
        vol_forecast = data['volatility_forecasting_models']
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=vol_forecast.index, y=vol_forecast['Realized_Vol_20D'],
                                name='Realized', line=dict(color='#1E3A8A')))
        fig.add_trace(go.Scatter(x=vol_forecast.index, y=vol_forecast['EWMA_Forecast'],
                                name='EWMA', line=dict(color='#10B981', dash='dash')))
        fig.add_trace(go.Scatter(x=vol_forecast.index, y=vol_forecast['GARCH_Forecast'],
                                name='GARCH', line=dict(color='#F59E0B', dash='dot')))
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)

elif page == "📐 Factor Analysis":
    st.header("📐 Factor Risk Attribution")
    
    if not data['barra_factors'].empty:
        factors = data['barra_factors']
        fig = px.bar(factors, x='Factor', y='Contribution_to_Risk',
                    color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(factors, use_container_width=True, hide_index=True)

elif page == "⚖️ Optimization":
    st.header("⚖️ Portfolio Optimization")
    
    if not data['grinold_kahn_strategies'].empty:
        gk = data['grinold_kahn_strategies']
        fig = px.bar(gk, x='Strategy', y='Expected_IR',
                    color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        st.plotly_chart(fig, use_container_width=True)
        
        st.dataframe(gk, use_container_width=True, hide_index=True)

elif page == "🏪 ETF Flow":
    st.header("🏪 ETF Microstructure")
    
    if not data['etf_arbitrage_microstructure'].empty:
        etf = data['etf_arbitrage_microstructure'].tail(100)
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=etf.index, y=etf['Premium_Discount_bps'],
                                line=dict(color='#1E3A8A')))
        fig.update_layout(height=400, plot_bgcolor='white', title="Premium/Discount")
        st.plotly_chart(fig, use_container_width=True)

elif page == "🌊 Order Flow":
    st.header("🌊 Order Flow Toxicity")
    
    if not data['order_flow_toxicity'].empty:
        toxicity = data['order_flow_toxicity']
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=toxicity.index, y=toxicity['VPIN'],
                                line=dict(color='#1E3A8A')))
        fig.add_hline(y=0.55, line_dash="dash", line_color="red")
        fig.update_layout(height=400, plot_bgcolor='white', title="VPIN")
        st.plotly_chart(fig, use_container_width=True)

elif page == "🤖 ML Alpha":
    st.header("🤖 ML Alpha Factors")
    
    if not data['ml_feature_importance'].empty:
        ml_imp = data['ml_feature_importance']
        fig = px.bar(ml_imp, x='Feature', y='Random_Forest_Importance',
                    color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)

elif page == "🎲 Greeks":
    st.header("🎲 Dynamic Hedging & Greeks")
    
    if not data['option_greeks_dynamic_hedging'].empty:
        greeks = data['option_greeks_dynamic_hedging'].tail(60)
        
        col1, col2 = st.columns(2)
        with col1:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=greeks.index, y=greeks['Total_Vega'],
                                    line=dict(color='#1E3A8A')))
            fig.update_layout(height=300, plot_bgcolor='white', title="Vega")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=greeks.index, y=greeks['Total_PnL'],
                                    line=dict(color='#10B981')))
            fig.update_layout(height=300, plot_bgcolor='white', title="P&L")
            st.plotly_chart(fig, use_container_width=True)

elif page == "📅 Economic Calendar":
    st.header("📅 Economic Calendar")
    
    if not data['economic_calendar'].empty:
        calendar = data['economic_calendar']
        st.dataframe(calendar[['Event_Date', 'Event_Name', 'Priority', 
                              'Days_Until', 'Avg_VIX_Move_Historical']],
                    use_container_width=True, hide_index=True)

elif page == "🎨 3D Analytics":
    st.header("🎨 Advanced 3D Analytics")
    st.markdown("*Showcase of advanced 3D visualizations*")
    
    st.subheader("Portfolio Greeks 3D Trajectory")
    if not data['option_greeks_dynamic_hedging'].empty:
        greeks = data['option_greeks_dynamic_hedging'].tail(100)
        
        fig = go.Figure()
        fig.add_trace(go.Scatter3d(
            x=greeks.index,
            y=greeks['Total_Vega'],
            z=greeks['Total_Gamma'],
            mode='lines+markers',
            marker=dict(size=3, color='#1E3A8A')
        ))
        
        fig.update_layout(
            scene=dict(
                xaxis_title='Time',
                yaxis_title='Vega',
                zaxis_title='Gamma'
            ),
            height=700
        )
        st.plotly_chart(fig, use_container_width=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748B; padding: 20px;'>
    <p><strong>Professional Volatility Analytics Platform</strong></p>
    <p>© 2025 | Educational Purposes</p>
</div>
""", unsafe_allow_html=True)
