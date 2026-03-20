import streamlit as st

def present_admin_cleanup(api):
    try:
        if not isinstance(api, dict):
            st.write(api)
            return

        col1, col2 = st.columns(2)
        active_admin_num = 0
        most_active_admin = ''

        with col1:
            st.write(f"Total Protections: {api.get('total_protections', 'N/A')}")
            st.write(f"Total Unprotections: {api.get('total_unprotect_protections', 'N/A')}")

            last_protection = api.get('last_protection')
            if last_protection:
                with st.expander('Show last protection?'):
                    st.write(f"User: {last_protection.get('user', 'N/A')}")
                    st.write(f"Type: {last_protection.get('type', 'N/A')}")
                    st.write(f"Action: {last_protection.get('action', 'N/A')}")
                    st.write(f"Timestamp: {last_protection.get('timestamp', 'N/A')}")
                    st.write(f"Comment: {last_protection.get('comment', 'N/A')}")

        with col2:
            st.write(f"Total Deletions: {api.get('total_deletions', 'N/A')}")
            st.write(f"Total Restores: {api.get('total_restores', 'N/A')}")

            last_deletion = api.get('last_deletion')
            if last_deletion:
                with st.expander('Show last deletion?'):
                    st.write(f"User: {last_deletion.get('user', 'N/A')}")
                    st.write(f"Type: {last_deletion.get('type', 'N/A')}")
                    st.write(f"Action: {last_deletion.get('action', 'N/A')}")
                    st.write(f"Timestamp: {last_deletion.get('timestamp', 'N/A')}")
                    st.write(f"Comment: {last_deletion.get('comment', 'N/A')}")

        active_admin = api.get('active_admin', {})
        if isinstance(active_admin, dict):
            for admin, value in active_admin.items():
                if isinstance(value, (int, float)) and value > active_admin_num:
                    active_admin_num = value
                    most_active_admin = admin

        st.write(f"Most Active Admin: {most_active_admin or 'N/A'}")

    except Exception as exc:
        st.error('Unable to display admin cleanup data.')
        st.exception(exc)