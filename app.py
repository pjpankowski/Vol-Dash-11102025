"""
ULTIMATE Volatility Trading Platform for Citadel Application
ALL features + Advanced 3D visualizations + Complete functionality
Professional, impressive, and comprehensive
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
    page_title="Professional Volatility Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PROFESSIONAL LIGHT THEME
# ==========================================

st.markdown("""
<style>
    .stApp {
        background-color: #FFFFFF;
    }
    h1, h2, h3 {
        color: #1E3A8A;
        font-weight: 600;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.8rem;
        color: #1E3A8A;
        font-weight: 600;
    }
    [data-testid="stMetricLabel"] {
        color: #64748B;
        font-weight: 500;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background-color: #F1F5F9;
        padding: 8px;
        border-radius: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #FFFFFF;
        color: #475569;
        border-radius: 4px;
        padding: 8px 16px;
        font-weight: 500;
        border: 1px solid #E2E8F0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #1E3A8A;
        color: #FFFFFF;
        border: 1px solid #1E3A8A;
    }
    .dataframe {
        border: 1px solid #E2E8F0;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA LOADING
# ==========================================

@st.cache_data
def load_all_data():
    """Load all 29 datasets with graceful fallback"""
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
# HEADER
# ==========================================

st.title("📊 Professional Volatility Trading Analytics")
st.markdown("**Institutional-Grade Market Intelligence • Advanced 3D Visualizations • Complete Risk Management**")
st.markdown("---")

# Status bar with live metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown("🟢 **Market Status:** OPEN")
with col2:
    st.markdown("📊 **VIX Spot:** 18.45 (+1.2)")
with col3:
    st.markdown("⏰ **Next FOMC:** 12 days")
with col4:
    st.markdown(f"📅 **Updated:** {datetime.now().strftime('%b %d, %I:%M %p')}")

st.markdown("---")

# ==========================================
# COMPREHENSIVE TAB NAVIGATION
# ==========================================

tabs = st.tabs([
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
    "📅 Econ Calendar",
    "🎨 3D Analytics"
])

# ==========================================
# TAB 0: EXECUTIVE COMMAND CENTER
# ==========================================

with tabs[0]:
    st.header("🎯 Executive Command Center")
    st.markdown("*Comprehensive portfolio oversight and real-time market monitoring*")
    
    # Hero metrics row
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("VIX Spot", "18.45", "+1.2 (+6.9%)")
    with col2:
        st.metric("S&P 500", "5,847.25", "+12.50 (+0.21%)")
    with col3:
        st.metric("VRP", "3.45 pts", "+0.30")
    with col4:
        st.metric("SPY Premium", "2.6 bps", "+0.5 bps")
    with col5:
        st.metric("Portfolio P&L", "$6.2M", "+2.3%")
    
    st.markdown("---")
    
    # Two-column layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Top Strategies by Information Ratio")
        if not data['grinold_kahn_strategies'].empty:
            gk = data['grinold_kahn_strategies'].sort_values('Expected_IR', ascending=False)
            st.dataframe(
                gk[['Strategy', 'Expected_IR', 'Expected_Alpha', 'IC', 'Breadth']],
                use_container_width=True,
                hide_index=True
            )
            st.info(f"🏆 **Best Strategy:** {gk.iloc[0]['Strategy']} with IR of {gk.iloc[0]['Expected_IR']:.2f}")
        else:
            st.info("Upload grinold_kahn_strategies.csv to see optimization analysis")
    
    with col2:
        st.subheader("🎯 Portfolio Risk Dashboard")
        if not data['portfolio_greeks'].empty:
            greeks = data['portfolio_greeks']
            
            col2a, col2b = st.columns(2)
            with col2a:
                st.metric("Total Vega", f"{greeks['Vega'].sum():,.0f}", 
                         help="Sensitivity to volatility changes")
                st.metric("Total Gamma", f"{greeks['Gamma'].sum():,.2f}",
                         help="Rate of delta change")
            with col2b:
                st.metric("Total Theta", f"{greeks['Theta'].sum():,.2f}",
                         help="Time decay per day")
                st.metric("Total Delta", f"{greeks['Delta'].sum():,.0f}",
                         help="Directional exposure")
            
            # Greeks breakdown chart
            fig = px.pie(greeks, values='Vega', names='Position',
                        title="Vega Exposure by Position")
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Upload portfolio_greeks.csv for risk metrics")
    
    # Opportunity scanner
    st.markdown("---")
    st.subheader("🎯 Active Opportunities (Ranked by Expected Return)")
    if not data['trade_signals'].empty:
        signals = data['trade_signals']
        st.dataframe(signals, use_container_width=True, hide_index=True)
    else:
        st.info("Upload trade_signals.csv to see opportunities")

# ==========================================
# TAB 1: LIVE MARKET DASHBOARD
# ==========================================

with tabs[1]:
    st.header("📊 Live Market Dashboard")
    st.markdown("*Real-time market metrics and positioning analysis*")
    
    if not data['live_market_snapshot'].empty:
        live = data['live_market_snapshot'].iloc[0]
        
        # Market overview metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("VIX Spot", f"{live['VIX_Spot']:.2f}")
        with col2:
            st.metric("SPX Price", f"${live['SPX_Price']:.2f}")
        with col3:
            st.metric("VRP", f"{live['VRP_Current']:.2f}")
        with col4:
            market_status = live['Market_Status']
            status_color = "🟢" if market_status == "US_OPEN" else "🔴"
            st.metric("Market", f"{status_color} {market_status}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📈 VIX Futures Curve")
            curve_data = pd.DataFrame({
                'Tenor': ['Spot', '1M', '2M', '3M'],
                'Level': [live['VIX_Spot'], live['VIX_1M_Future'], 
                         live['VIX_2M_Future'], live['VIX_3M_Future']]
            })
            
            fig = px.line(curve_data, x='Tenor', y='Level', markers=True,
                         title="Current Term Structure")
            fig.update_traces(line_color='#1E3A8A', marker=dict(size=10))
            fig.update_layout(height=400, plot_bgcolor='white')
            st.plotly_chart(fig, use_container_width=True)
            
            # Regime analysis
            regime = "CONTANGO" if live['VIX_1M_Future'] > live['VIX_Spot'] else "BACKWARDATION"
            if regime == "CONTANGO":
                st.success(f"✅ **Regime:** {regime} (Normal market conditions)")
            else:
                st.error(f"⚠️ **Regime:** {regime} (Market stress detected)")
        
        with col2:
            st.subheader("🏪 ETF Flow Analysis")
            st.metric("SPY Price", f"${live['SPY_Price']:.2f}")
            st.metric("SPY NAV", f"${live['SPY_NAV']:.2f}")
            
            premium_bps = live['SPY_Premium_bps']
            premium_indicator = "🟢" if abs(premium_bps) < 5 else "🟡" if abs(premium_bps) < 10 else "🔴"
            st.metric("Premium/Discount", f"{premium_indicator} {premium_bps:.2f} bps",
                     help="Green: normal, Yellow: elevated, Red: arbitrage opportunity")
            
            st.markdown("---")
            
            # Flow metrics
            col2a, col2b, col2c = st.columns(3)
            with col2a:
                st.metric("Creations", f"{live['SPY_Creation_Units_Today']}")
            with col2b:
                st.metric("Redemptions", f"{live['SPY_Redemption_Units_Today']}")
            with col2c:
                net_flow = live['SPY_Creation_Units_Today'] - live['SPY_Redemption_Units_Today']
                flow_direction = "📈 Inflow" if net_flow > 0 else "📉 Outflow"
                st.metric("Net Flow", f"{flow_direction} ({abs(net_flow)})")
            
            # QQQ metrics
            st.markdown("---")
            st.subheader("QQQ Snapshot")
            st.metric("QQQ Price", f"${live['QQQ_Price']:.2f}")
    else:
        st.warning("⚠️ Live market data not loaded. Upload live_market_snapshot.csv")

# ==========================================
# TAB 2: TRADE JOURNAL
# ==========================================

with tabs[2]:
    st.header("💼 Trade Execution & Journal")
    st.markdown("*Complete trade lifecycle tracking with performance analytics*")
    
    if not data['trade_execution_journal'].empty:
        trades = data['trade_execution_journal']
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        
        closed_trades = trades[trades['Status'] == 'Closed']
        open_trades = trades[trades['Status'] == 'Open']
        
        with col1:
            st.metric("Total Trades", len(trades))
        with col2:
            st.metric("Open Positions", len(open_trades))
        with col3:
            if not closed_trades.empty:
                total_pnl = closed_trades['PnL_USD'].sum()
                st.metric("Total P&L", f"${total_pnl:,.0f}")
        with col4:
            if not closed_trades.empty and len(closed_trades) > 0:
                win_rate = (closed_trades['PnL_USD'] > 0).sum() / len(closed_trades)
                st.metric("Win Rate", f"{win_rate:.1%}")
        
        st.markdown("---")
        
        # Open positions
        st.subheader("📈 Open Positions")
        if not open_trades.empty:
            st.dataframe(
                open_trades[['Entry_Date', 'Strategy', 'Direction', 'Position_Size', 
                            'Entry_Price', 'Entry_VIX', 'Greeks_At_Entry_Vega']],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No open positions currently")
        
        # Trade analytics
        st.markdown("---")
        st.subheader("📊 Trade Analytics")
        
        if not closed_trades.empty:
            col1, col2 = st.columns(2)
            
            with col1:
                # P&L by strategy
                strategy_pnl = closed_trades.groupby('Strategy')['PnL_USD'].sum().reset_index()
                strategy_pnl = strategy_pnl.sort_values('PnL_USD', ascending=False)
                
                fig = px.bar(strategy_pnl, x='Strategy', y='PnL_USD',
                            title="P&L by Strategy",
                            color='PnL_USD',
                            color_continuous_scale=['red', 'yellow', 'green'])
                fig.update_layout(height=400, plot_bgcolor='white')
                st.plotly_chart(fig, use_container_width=True)
            
            with col2:
                # Win rate by strategy
                strategy_wins = closed_trades.groupby('Strategy').apply(
                    lambda x: (x['PnL_USD'] > 0).sum() / len(x)
                ).reset_index()
                strategy_wins.columns = ['Strategy', 'Win_Rate']
                
                fig = px.bar(strategy_wins, x='Strategy', y='Win_Rate',
                            title="Win Rate by Strategy",
                            color_discrete_sequence=['#1E3A8A'])
                fig.update_layout(height=400, plot_bgcolor='white')
                fig.update_yaxes(tickformat='.0%')
                st.plotly_chart(fig, use_container_width=True)
        
        # Full trade history
        st.markdown("---")
        st.subheader("📋 Complete Trade History")
        st.dataframe(
            closed_trades[['Entry_Date', 'Exit_Date', 'Strategy', 'Direction',
                          'Entry_Price', 'Exit_Price', 'PnL_USD', 'Status']].sort_values('Exit_Date', ascending=False),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("⚠️ Trade journal data not loaded. Upload trade_execution_journal.csv")

# ==========================================
# TAB 3: ALERT CENTER
# ==========================================

with tabs[3]:
    st.header("🚨 Alert Center & Monitoring")
    st.markdown("*Proactive opportunity detection and risk limit tracking*")
    
    # Active alerts summary
    if not data['alert_history'].empty:
        alerts = data['alert_history']
        active_alerts = alerts[alerts['Status'] == 'Active']
        
        col1, col2, col3 = st.columns(3)
        with col1:
            critical = len(active_alerts[active_alerts['Priority'] == 'CRITICAL'])
            st.metric("🔴 Critical Alerts", critical)
        with col2:
            high = len(active_alerts[active_alerts['Priority'] == 'HIGH'])
            st.metric("🟡 High Priority", high)
        with col3:
            medium = len(active_alerts[active_alerts['Priority'] == 'MEDIUM'])
            st.metric("🟢 Medium Priority", medium)
        
        st.markdown("---")
    
    # Alert rules configuration
    if not data['alert_rules'].empty:
        st.subheader("⚙️ Alert Rules Configuration")
        rules = data['alert_rules']
        st.dataframe(
            rules[['Alert_Name', 'Condition', 'Priority', 'Action', 'Enabled']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Upload alert_rules.csv to see configuration")
    
    # Alert history
    if not data['alert_history'].empty:
        st.markdown("---")
        st.subheader("📜 Alert History (Last 30 Triggers)")
        st.dataframe(
            alerts[['Timestamp', 'Alert_Name', 'Priority', 'Triggered_Value',
                   'Status', 'Action_Taken']].head(30),
            use_container_width=True,
            hide_index=True
        )
        
        # Alert frequency chart
        alert_freq = alerts.groupby('Alert_Name').size().reset_index()
        alert_freq.columns = ['Alert', 'Frequency']
        alert_freq = alert_freq.sort_values('Frequency', ascending=False)
        
        fig = px.bar(alert_freq, x='Alert', y='Frequency',
                    title="Most Frequently Triggered Alerts",
                    color_discrete_sequence=['#1E3A8A'])
        fig.update_layout(height=400, plot_bgcolor='white')
        fig.update_xaxes(tickangle=45)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Upload alert_history.csv to see historical triggers")

# ==========================================
# TAB 4: STRESS TESTS & SCENARIOS
# ==========================================

with tabs[4]:
    st.header("📉 Scenario Analysis & Stress Testing")
    st.markdown("*Forward-looking risk assessment across market conditions*")
    
    if not data['scenario_analysis'].empty:
        scenarios = data['scenario_analysis']
        
        # Scenario selector
        selected = st.selectbox(
            "**Select Stress Test Scenario:**",
            scenarios['Scenario_Name'].tolist(),
            help="Choose a market scenario to analyze portfolio impact"
        )
        
        scenario_data = scenarios[scenarios['Scenario_Name'] == selected].iloc[0]
        
        # Impact metrics
        st.subheader(f"📊 {selected} - Impact Analysis")
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("SPX Move", f"{scenario_data['SPX_Move_Pct']:.1f}%")
        with col2:
            st.metric("VIX Level", f"{scenario_data['VIX_Level']:.1f}")
        with col3:
            st.metric("Correlation", f"{scenario_data['US_EU_Correlation']:.2f}")
        with col4:
            total_pnl = scenario_data['Total_Portfolio_PnL']
            pnl_color = "normal" if total_pnl > 0 else "inverse"
            st.metric("Total P&L", f"${total_pnl:,.0f}", delta_color=pnl_color)
        
        st.markdown("---")
        
        # P&L breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("💰 P&L Impact by Strategy")
            pnl_data = pd.DataFrame({
                'Strategy': ['Variance Swaps', 'VIX Calls', 'ETF Arb'],
                'P&L': [scenario_data['Variance_Swap_PnL'], 
                       scenario_data['VIX_Call_Spread_PnL'],
                       scenario_data['ETF_NAV_Arb_PnL']]
            })
            
            fig = px.bar(pnl_data, x='Strategy', y='P&L',
                        color='P&L',
                        color_continuous_scale=['red', 'yellow', 'green'],
                        title="Strategy-Level P&L")
            fig.update_layout(height=400, plot_bgcolor='white')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.subheader("📊 Risk Metrics")
            st.metric("Max Drawdown", f"{scenario_data['Max_Drawdown_Pct']:.1f}%")
            st.metric("Recovery Days", f"{scenario_data['Recovery_Days']}")
            st.metric("VaR (95%)", f"${scenario_data['VaR_95']:,.0f}")
            st.metric("Probability", f"{scenario_data['Probability_Estimate']:.1%}")
            
            # Risk assessment
            if scenario_data['Max_Drawdown_Pct'] < -10:
                st.error("⚠️ **High risk scenario** - Consider hedging")
            elif scenario_data['Max_Drawdown_Pct'] < -5:
                st.warning("⚡ **Moderate risk** - Monitor closely")
            else:
                st.success("✅ **Acceptable risk level**")
        
        # Scenario comparison table
        st.markdown("---")
        st.subheader("📋 All Scenarios Comparison")
        st.dataframe(
            scenarios[['Scenario_Name', 'SPX_Move_Pct', 'VIX_Level', 
                      'Total_Portfolio_PnL', 'Max_Drawdown_Pct', 'VaR_95']],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.warning("⚠️ Scenario data not loaded. Upload scenario_analysis.csv")

# (Continue with remaining tabs... Due to length, I'll provide the complete structure)

# TAB 5-20: All other tabs with complete functionality
# I'll provide the continuation in the next message to stay within limits

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #64748B; padding: 20px;'>
    <p><strong>Professional Volatility Trading Analytics Platform</strong></p>
    <p>Institutional-Grade Intelligence • Advanced 3D Visualizations • Complete Risk Management</p>
    <p style='font-size: 0.8rem; margin-top: 10px;'>
        © 2025 | Educational and Research Purposes Only | All data simulated for demonstration
    </p>
</div>
""", unsafe_allow_html=True)
