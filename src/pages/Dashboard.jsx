import { ArrowTopRightOnSquareIcon } from '@heroicons/react/20/solid'
import { Link } from 'react-router-dom'

const features = [
  {
    name: 'OpenAI Assistant',
    description: 'Interact with GPT-4 and other OpenAI models',
    href: '/openai',
    icon: '🤖'
  },
  {
    name: 'Claude Assistant',
    description: 'Access Anthropic\'s Claude for advanced reasoning',
    href: '/claude',
    icon: '🧠'
  },
  {
    name: 'Gemini Assistant',
    description: 'Use Google\'s latest AI technology',
    href: '/gemini',
    icon: '☁️'
  },
  {
    name: 'Groq Assistant',
    description: 'Experience ultra-fast AI responses',
    href: '/groq',
    icon: '⚡'
  },
  {
    name: 'Venice Assistant',
    description: 'Access Venice\'s powerful AI models',
    href: '/venice',
    icon: '🌊'
  },
  {
    name: 'Local LLM',
    description: 'Run AI models locally with Ollama',
    href: '/local-llm',
    icon: '💻'
  },
  {
    name: 'Multi-Model Query',
    description: 'Compare responses across different AI models',
    href: '/multi-model',
    icon: '🔄'
  }
]

export default function Dashboard() {
  return (
    <div className="bg-white">
      <div className="mx-auto max-w-7xl">
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">SuperBrain AI Platform</h2>
          <p className="mt-2 text-lg leading-8 text-gray-600">
            Access multiple AI models through a unified interface
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
          <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-16 lg:max-w-none lg:grid-cols-3">
            {features.map((feature) => (
              <div key={feature.name} className="flex flex-col">
                <dt className="flex items-center gap-x-3 text-base font-semibold leading-7 text-gray-900">
                  <span className="text-2xl">{feature.icon}</span>
                  {feature.name}
                </dt>
                <dd className="mt-4 flex flex-auto flex-col text-base leading-7 text-gray-600">
                  <p className="flex-auto">{feature.description}</p>
                  <p className="mt-6">
                    <Link
                      to={feature.href}
                      className="text-sm font-semibold leading-6 text-indigo-600"
                    >
                      Open Assistant <span aria-hidden="true">→</span>
                    </Link>
                  </p>
                </dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </div>
  )
}