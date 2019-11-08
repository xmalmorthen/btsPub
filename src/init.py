global __session__

__session__ = False

if __name__ == '__main__':
    from controllers import dashboard
    dashboard.vp_start_gui()
