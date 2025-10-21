from typing import Optional
from openai import AsyncOpenAI
from anthropic import AsyncAnthropic
import httpx

async def generate_article_content(
    brief: str,
    ai_model,
    profile_content: Optional[str] = None
) -> str:
    """
    调用AI模型生成文章内容

    Args:
        brief: 需求描述
        ai_model: AIModel数据库模型实例
        profile_content: 可选的写作风格配置

    Returns:
        生成的文章内容
    """
    # 构建提示词
    prompt = f"请根据以下需求生成文章：\n\n{brief}"

    if profile_content:
        prompt = f"请按照以下写作风格配置生成文章：\n\n{profile_content}\n\n需求：\n{brief}"

    provider = ai_model.provider.lower()

    try:
        if provider == "openai":
            return await _call_openai(ai_model, prompt)
        elif provider == "anthropic":
            return await _call_anthropic(ai_model, prompt)
        elif provider in ["文心一言", "通义千问", "智谱ai", "豆包"]:
            return await _call_chinese_ai(ai_model, prompt)
        else:
            # 其他模型，尝试使用OpenAI兼容接口
            return await _call_openai(ai_model, prompt)
    except Exception as e:
        raise Exception(f"AI生成失败: {str(e)}")


async def _call_openai(ai_model, prompt: str) -> str:
    """调用OpenAI API"""
    client = AsyncOpenAI(
        api_key=ai_model.api_key,
        base_url=ai_model.base_url if ai_model.base_url else None
    )

    response = await client.chat.completions.create(
        model=ai_model.model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=ai_model.temperature,
        max_tokens=ai_model.max_tokens
    )

    return response.choices[0].message.content


async def _call_anthropic(ai_model, prompt: str) -> str:
    """调用Anthropic Claude API"""
    client = AsyncAnthropic(api_key=ai_model.api_key)

    response = await client.messages.create(
        model=ai_model.model_name,
        max_tokens=ai_model.max_tokens,
        temperature=ai_model.temperature,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


async def _call_chinese_ai(ai_model, prompt: str) -> str:
    """
    调用国产AI模型（文心一言、通义千问等）
    这些模型通常提供OpenAI兼容的接口
    """
    # 大多数国产AI都提供了OpenAI兼容接口
    if not ai_model.base_url:
        raise ValueError(f"{ai_model.provider} 需要配置 base_url")

    client = AsyncOpenAI(
        api_key=ai_model.api_key,
        base_url=ai_model.base_url
    )

    response = await client.chat.completions.create(
        model=ai_model.model_name,
        messages=[{"role": "user", "content": prompt}],
        temperature=ai_model.temperature,
        max_tokens=ai_model.max_tokens
    )

    return response.choices[0].message.content
