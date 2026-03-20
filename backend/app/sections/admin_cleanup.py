import streamlit as st

def present_admin_cleanup(api):
    col1, col2 = st.columns(2)
    active_admin_num = 0
    active_admin = ''

    with col1:
        st.write(f'Total Protections: {api['total_protections']}')
        st.write(f'Total Unprotections: {api['total_unprotect_protections']}')
        
        with st.expander('Show last protections?'):
            last_protection = api['last_protection']

            st.write(f'User: {last_protection['user']}')
            st.write(f'Type: {last_protection['type']}')
            st.write(f'Action: {last_protection['action']}')
            st.write(f'Timestamp: {last_protection['timestamp']}')
            st.write(f'Comment: {last_protection['comment']}')

    with col2:
        st.write(f'Total Deletions: {api['total_deletions']}')
        st.write(f'Total Restores: {api['total_restores']}')
        
        with st.expander('Show last delete?'):
            last_protection = api['last_deletion']

            st.write(f'User: {last_protection['user']}')
            st.write(f'Type: {last_protection['type']}')
            st.write(f'Action: {last_protection['action']}')
            st.write(f'Timestamp: {last_protection['timestamp']}')
            st.write(f'Comment: {last_protection['comment']}')
        
    active_admin = api['active_admin']
    for admin, value in active_admin.items():
        if value > active_admin_num:
            active_admin_num = value
            active_admin = admin

    st.write(f'Most Active Admin: {active_admin}')