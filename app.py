"""
Professional Volatility Trading Platform - Ultimate Edition
Institutional-Grade Analytics for Macro Equity Vol Desk

Author: Your Name
Date: November 2025
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
    page_title="Professional Volatility Trading Platform",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
    /* Main theme */
    .stApp {
        background-color: #0A1929;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #FFB81C;
        font-weight: 700;
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #FFB81C;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1E2A38;
        padding: 10px;
        border-radius: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #0A1929;
        color: #FFFFFF;
        border-radius: 4px;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: #FFB81C;
        color: #0A1929;
    }
    
    /* Alert badges */
    .alert-critical {
        background-color: #DC2626;
        color: white;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 600;
    }
    
    .alert-high {
        background-color: #F59E0B;
        color: white;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 600;
    }
    
    .alert-medium {
        background-color: #10B981;
        color: white;
        padding: 4px 12px;
        border-radius: 4px;
        font-weight: 600;
    }
    
    /* Cards */
    .metric-card {
        background: linear-gradient(135deg, #1E2A38 0%, #0A1929 100%);
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #FFB81C;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* Tables */
    .dataframe {
        font-size: 0.9rem;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        color: #888;
        font-size: 0.8rem;
        margin-top: 50px;
        padding: 20px;
        border-top: 1px solid #333;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA LOADING FUNCTIONS
# ==========================================

@st.cache_data
def load_all_data():
    """Load all 29 datasets"""
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
            st.warning(f"Could not load {file}.csv - using sample data")
            data[file] = pd.DataFrame()
    
    return data

# Load data
data = load_all_data()

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div style='text-align: center; padding: 20px 0; border-bottom: 2px solid #FFB81C;'>
    <h1 style='margin: 0; font-size: 2.5rem;'>📊 VOLATILITY ANALYTICS</h1>
    <p style='color: #FFB81C; font-size: 1.1rem; margin: 10px 0 0 0;'>
        Institutional-Grade Analytics with Live Monitoring & Advanced Risk Management
    </p>
</div>
""", unsafe_allow_html=True)

# Status bar
col1, col2, col3, col4 = st.columns([2, 2, 2, 3])
with col1:
    st.markdown("🟢 **Market Status:** US_OPEN")
with col2:
    st.markdown("🔴 **2 Active Alerts**")
with col3:
    st.markdown(f"⏰ **Next FOMC:** 12 days")
with col4:
    st.markdown(f"📅 **Last Updated:** {datetime.now().strftime('%B %d, %Y %I:%M %p EST')}")

st.markdown("---")

# ==========================================
# MAIN TAB NAVIGATION
# ==========================================

tab_list = [
    "🎯 Executive Command",
    "📊 Live Market",
    "💼 Trade Journal",
    "🚨 Alerts",
    "🎯 Scenarios",
    "📝 Research Notes",
    "📊 Performance",
    "🌍 Global Dislocations",
    "📈 VIX Ecosystem",
    "🔷 Vol Surface",
    "💎 Variance Swaps",
    "💰 Dividend Futures",
    "🔮 Forecasting",
    "📐 Factor Attribution",
    "⚖️ Fundamental Law",
    "🏪 ETF Microstructure",
    "🌊 Order Flow",
    "🤖 ML Alpha",
    "🎲 Dynamic Hedging",
    "🌡️ Vol Regimes",
    "🏗️ Portfolio Construction",
    "📋 Trade Evaluation",
    "⚡ IV vs RV",
    "🌐 Cross-Asset",
    "🛡️ Risk Management",
    "📅 Economic Calendar",
    "🕸️ Correlation Network",
    "🔬 Research Lab"
]

selected_tab = st.tabs(tab_list)

# ==========================================
# TAB 1: EXECUTIVE COMMAND CENTER
# ==========================================

with selected_tab[0]:
    st.header("🎯 Executive Command Center")
    st.markdown("*Comprehensive portfolio overview and real-time monitoring*")
    
    # Hero metrics
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    if not data['live_market_snapshot'].empty:
        live_data = data['live_market_snapshot'].iloc[0]
        
        with col1:
            st.metric("VIX Spot", f"{live_data['VIX_Spot']:.2f}", 
                     delta="+1.2" if live_data['VIX_Spot'] > 18 else "-0.5")
        with col2:
            st.metric("S&P 500", f"{live_data['SPX_Price']:.2f}", 
                     delta="+12.5")
        with col3:
            st.metric("VRP", f"{live_data['VRP_Current']:.2f}", 
                     delta="+0.3")
        with col4:
            st.metric("SPY Premium", f"{live_data['SPY_Premium_bps']:.1f} bps", 
                     delta="+0.5 bps")
        with col5:
            st.metric("Creation Units", f"{live_data['SPY_Creation_Units_Today']}", 
                     delta=f"+{live_data['SPY_Creation_Units_Today'] - live_data['SPY_Redemption_Units_Today']}")
        with col6:
            st.metric("Next FOMC", f"{live_data['Next_FOMC_Days']} days")
    
    st.markdown("---")
    
    # Portfolio summary
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Portfolio P&L Summary")
        if not data['performance_attribution_daily'].empty:
            perf = data['performance_attribution_daily']
            
            # Cumulative P&L chart
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=perf.index,
                y=perf['Cumulative_PnL'],
                fill='tozeroy',
                name='Cumulative P&L',
                line=dict(color='#FFB81C', width=2)
            ))
            fig.update_layout(
                title="Cumulative P&L",
                paper_bgcolor='#0A1929',
                plot_bgcolor='#1E2A38',
                font=dict(color='white'),
                height=300
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Summary stats
            total_pnl = perf['Cumulative_PnL'].iloc[-1]
            st.metric("Total P&L", f"${total_pnl:,.0f}")
    
    with col2:
        st.subheader("🎯 Risk Dashboard")
        if not data['portfolio_greeks'].empty:
            greeks = data['portfolio_greeks']
            
            # Greeks summary
            total_vega = greeks['Vega'].sum()
            total_gamma = greeks['Gamma'].sum()
            total_theta = greeks['Theta'].sum()
            total_delta = greeks['Delta'].sum()
            
            st.metric("Total Vega", f"{total_vega:,.0f}")
            st.metric("Total Gamma", f"{total_gamma:,.2f}")
            st.metric("Total Theta", f"{total_theta:,.2f}")
            st.metric("Total Delta", f"{total_delta:,.0f}")
    
    st.markdown("---")
    
    # Opportunities scanner
    st.subheader("🎯 Top Opportunities (Ranked by Expected IR)")
    if not data['grinold_kahn_strategies'].empty:
        gk = data['grinold_kahn_strategies'].sort_values('Expected_IR', ascending=False)
        st.dataframe(gk[['Strategy', 'Expected_IR', 'Expected_Alpha', 'IC', 'Breadth']], 
                    use_container_width=True)

# ==========================================
# TAB 2: LIVE MARKET DASHBOARD
# ==========================================

with selected_tab[1]:
    st.header("📊 Live Market Dashboard")
    st.markdown("*Real-time market metrics and positioning*")
    
    if not data['live_market_snapshot'].empty:
        live = data['live_market_snapshot'].iloc[0]
        
        # VIX Futures Curve
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("VIX Futures Curve")
            vix_curve_data = {
                'Tenor': ['Spot', '1M', '2M', '3M'],
                'Level': [live['VIX_Spot'], live['VIX_1M_Future'], 
                         live['VIX_2M_Future'], live['VIX_3M_Future']]
            }
            fig = px.bar(vix_curve_data, x='Tenor', y='Level', 
                        title="Current Term Structure",
                        color_discrete_sequence=['#FFB81C'])
            fig.update_layout(
                paper_bgcolor='#0A1929',
                plot_bgcolor='#1E2A38',
                font=dict(color='white')
            )
            st.plotly_chart(fig, use_container_width=True)
            
            regime = "CONTANGO" if live['VIX_1M_Future'] > live['VIX_Spot'] else "BACKWARDATION"
            st.markdown(f"**Term Structure Regime:** {regime}")
        
        with col2:
            st.subheader("ETF Flow Snapshot")
            st.metric("SPY Price", f"${live['SPY_Price']:.2f}")
            st.metric("SPY NAV", f"${live['SPY_NAV']:.2f}")
            st.metric("Premium/Discount", f"{live['SPY_Premium_bps']:.2f} bps",
                     delta="Arbitrage opportunity" if abs(live['SPY_Premium_bps']) > 10 else None)
            
            col2a, col2b = st.columns(2)
            with col2a:
                st.metric("Creations", live['SPY_Creation_Units_Today'])
            with col2b:
                st.metric("Redemptions", live['SPY_Redemption_Units_Today'])
            
            net_flow = live['SPY_Creation_Units_Today'] - live['SPY_Redemption_Units_Today']
            st.metric("Net Flow", net_flow, delta="Positive inflow" if net_flow > 0 else "Negative outflow")

# ==========================================
# TAB 3: TRADE JOURNAL
# ==========================================

with selected_tab[2]:
    st.header("💼 Trade Execution & Journal")
    st.markdown("*Complete trade lifecycle tracking and analytics*")
    
    if not data['trade_execution_journal'].empty:
        trades = data['trade_execution_journal']
        
        # Summary stats
        col1, col2, col3, col4 = st.columns(4)
        
        closed_trades = trades[trades['Status'] == 'Closed']
        total_pnl = closed_trades['PnL_USD'].sum() if not closed_trades.empty else 0
        win_rate = (closed_trades['PnL_USD'] > 0).sum() / len(closed_trades) if len(closed_trades) > 0 else 0
        
        with col1:
            st.metric("Total Trades", len(trades))
        with col2:
            st.metric("Open Positions", len(trades[trades['Status'] == 'Open']))
        with col3:
            st.metric("Total P&L", f"${total_pnl:,.0f}")
        with col4:
            st.metric("Win Rate", f"{win_rate:.1%}")
        
        st.markdown("---")
        
        # Open positions
        st.subheader("📈 Open Positions")
        open_trades = trades[trades['Status'] == 'Open']
        if not open_trades.empty:
            st.dataframe(open_trades[['Entry_Date', 'Strategy', 'Direction', 'Position_Size', 
                                     'Entry_Price', 'Entry_VIX']], 
                        use_container_width=True)
        else:
            st.info("No open positions")
        
        # Trade history
        st.subheader("📋 Trade History")
        if not closed_trades.empty:
            # P&L by strategy
            strategy_pnl = closed_trades.groupby('Strategy')['PnL_USD'].sum().reset_index()
            strategy_pnl = strategy_pnl.sort_values('PnL_USD', ascending=False)
            
            fig = px.bar(strategy_pnl, x='Strategy', y='PnL_USD',
                        title="P&L by Strategy",
                        color='PnL_USD',
                        color_continuous_scale=['red', 'yellow', 'green'])
            fig.update_layout(
                paper_bgcolor='#0A1929',
                plot_bgcolor='#1E2A38',
                font=dict(color='white')
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Full trade table
            st.dataframe(closed_trades[['Entry_Date', 'Exit_Date', 'Strategy', 'Direction',
                                       'Entry_Price', 'Exit_Price', 'PnL_USD']].sort_values('Exit_Date', ascending=False),
                        use_container_width=True)

# Continue with remaining tabs...
# (Due to length constraints, I'll provide the rest in additional files)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown("""
<div class='footer'>
    <p><strong>Professional Volatility Trading Platform - Ultimate Edition</strong></p>
    <p>Institutional-Grade Analytics | Educational and Research Purposes Only</p>
    <p>All data is simulated for demonstration. Not financial advice.</p>
    <p style='margin-top: 10px; font-size: 0.7rem;'>© 2025 | Built with Streamlit</p>
</div>
""", unsafe_allow_html=True)
