import { Link } from 'react-router-dom'
import Button from './Button'

export default function NavBar() {
    return (
        <>
            <nav className='bg-(--primary-color) px-5 py-3'>
                <div className='flex justify-between items-center'>
                    <div className='flex items-center'>
                        <img 
                            src="\wikiwatch-logo.png" 
                            alt="WikiWatch Logo" 
                            width={'25px'}
                        />
                        <h1
                            className='font-bold font-sans text-xl' 
                        >WikiWatch</h1>
                    </div>
                    <div>
                        <ul className='flex gap-x-3 font-semibold text-xs'>
                            <li><Link>Home</Link></li>
                            <li><Link>Problems</Link></li>
                            <li><Link>Solutions</Link></li>
                            <li><Link>FAQ's</Link></li>
                        </ul>
                    </div>
                    <div
                        className='flex gap-x-2 text-xs'
                    >
                        <Button
                            text='Login'
                        />
                        <Button
                            text='Get Started'
                        />
                    </div>
                </div>
            </nav>
        </>
    )
}